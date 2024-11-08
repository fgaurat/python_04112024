from glob import glob
from pprint import pprint
import re


def main():
    all_logs = glob('*.log')
    cpt_404 = 0
    for log_file in all_logs:
        with open(log_file) as f:
            for line in f:
                line = line.strip()
                # reg = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
                # reg = r"(^.+?)\s"
                reg = r"\"\s(\d{3})"
                result = re.findall(reg,line)
                # if "404" in result:
                #     cpt_404+=1
                
                cpt_404 = cpt_404+1 if "404" in result else cpt_404
                
                print(result)
    print(cpt_404)
                
if __name__=='__main__':
    main()
