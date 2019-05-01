class FileOwners:

    @staticmethod
    def group_by_owners(files):
        grouped_dict = {}
        for k,v in files.items():
            try:
                grouped_dict[v].append(k) 
            except:
                grouped_dict[v] = [k]
        return grouped_dict

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))
