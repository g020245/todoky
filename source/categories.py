from source.config import cfg
class Category(object):

    def __init__(self):
        pass
    
    def getCategoriesSection(self):
        # todo test
        # todo ref
        # todo doc
        return cfg.getValue('categories')
    
    def printShortCategoryDescription(self):
        # todo test
        # todo ref
        # todo doc
        
        tmp = []
        for i in self.getCategoriesSection():
            for k, v in i.items():
                dtemp = {
                    'short': v['short'],
                    'category': k,
                    'description': v['description']
                }
                tmp.append(dtemp)
        print(f"{'Short'.ljust(8, ' ')}{'Word'.ljust(15, ' ')}{'Description'.ljust(50, ' ')}")
        for i in tmp:
            print(f"{str(i['short']).ljust(8, ' ')}{str(i['category']).ljust(15, ' ')}{str(i['description']).ljust(50, ' ')} ")


                
        
    
cat = Category()
cat.printShortCategoryDescription()



