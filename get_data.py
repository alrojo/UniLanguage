import argparse
import gzip
import urllib.parse
import urllib.request

parser = argparse.ArgumentParser(description='Download the protein datasets')
parser.add_argument('--data', type=str, default='data/', help='location of the data ids')
parser.add_argument('--domain', choices=['euk','bac','arc','vir'], default='euk', help='domain of origin: "euk","bac","arc" or "vir"')
parser.add_argument('--complete', choices=['full','frag'], default='full', help='completeness of the protein: "full" or "frag"')
parser.add_argument('--quality', choices=['exp','pred'], default='exp', help='evidence of existence of the protein: "exp" or "pred"')
parser.add_argument('--all', help='downnloads all the data')

args = parser.parse_args()

all_domains = ['euk','bac','arc','vir']
all_complete = ['full','frag']
all_quality = ['exp','pred']


def download_set(loc,domain,complete,quality,dataset):
    url = 'https://www.uniprot.org/uploadlists/'
    query = [line.rstrip('\n') for line in gzip.open('%s/%s_%s_%s/%s_ids.txt.gz' % (loc,domain,complete,quality,dataset), 'rt')]
    
    n_total = len(query)
    
    n = 3000
    formated_file = open('%s/%s_%s_%s/%s.txt' % (loc,domain,complete,quality,dataset),'w')
    
    i = 0
    while i*n < n_total:
        tmp_query = query[i*n:i*n+n]
        tmp_query = ' '.join(tmp_query)
        params = {
        'from': 'ACC+ID',
        'to': 'ACC',
        'format': 'tab',
         'columns': 'sequence',
        'query': tmp_query
        }
        
        data = urllib.parse.urlencode(params)
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data)

        with urllib.request.urlopen(req) as f:
            f.readline()
            for line in f:
                line = line.decode('utf-8').strip().split('\t')
                seq = ' '.join(list(line[0]))
                formated_file.write('%s\n' % seq)

        i += 1
    formated_file.close()
    


if args.all:
    print('Downloading all the data...')
    for domain in all_domains:
        for complete in all_complete:
            for quality in all_quality:
                download_set(args.data,domain,complete,quality,'train')
                download_set(args.data,domain,complete,'exp','valid')
                download_set(args.data,domain,complete,'exp','test') 

else:
    print('Downloading %s %s %s train, valid and test sets...' % (args.domain, args.complete, args.quality))
    download_set(args.data,args.domain,args.complete,args.quality,'train')
    download_set(args.data,args.domain,args.complete,'exp','valid')
    download_set(args.data,args.domain,args.complete,'exp','test')  


print('Download complete')
