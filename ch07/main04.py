import json

def main():
    all_json_data = []
    with open("MOCK_DATA.csv") as f:
        lines = f.readlines()
        # clear lines
        lines = [line.strip() for line in lines]
        header = lines[0].split(",")
        # region old code
        # for line in lines[1:]:
        #     data = line.split(',')
        #     for position,current_data in enumerate(data):
        #         print(header[position],current_data,sep=":",end=" ")
        #     print()
        # endregion
        
        for line in lines[1:]:
            data = line.split(',')
            data_dict = dict(zip(header,data))
            all_json_data.append(data_dict)
            # for header_name, current_data in zip(header,data):
            #     print(header_name,current_data,sep=":",end=" ")
            # print()
    
    
    with open('customers.json','w') as f:
        json.dump(all_json_data,f)    
if __name__=='__main__':
    
    main()