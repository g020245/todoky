

class Category(object):
    def __init__(self):
        pass

    def getActiveCategoryListShort(self) -> dict:
        # todo ref

        '''
        Get all categoreis in given in config. Returns {}
        {11: {'short_description': 'Private TODO', 'description': 'Saker relaterade till församlingshemmet i Hedemora.', 'type': 1, 'reserved': None}}
        :return:
        '''
        return cfg.getSetting('active_categories')

    def getActiveCategoryCount(self) -> int:

        '''
        Return a number of how many categories are in active_categories category in conf.
        :return:
        '''
        return len(self.getActiveCategoryListShort().keys())

    def getHighPrioCategory(self) -> str:

        '''
        Get High prio short category.
        :return:
        '''

        return cfg.getSetting('high_prio')

    def getCategoryListWithoutHighPrio(self) -> list:
        '''
        Make list of string of short categories without high prio category
        ['11', '22', '33', '44']
        :return:
        '''
        return [str(x) for x in self.getActiveCategoryListShort()]

    def getShortCategoryDescription(self, shortCat: str) -> [str, None]:

        # todo ref

        """
        Get short description of category alias provided.
        :param cat:
        :return:
        """
        if shortCat.strip() in self.getCategoryListWithoutHighPrio():
            return str(
                cfg.getSetting('active_categories', str(shortCat), 'short_description'))
        else:
            return 'There is no such category defined'

    def isPublicCategory(self, type: int) -> bool:
        # todo test
        # todo ref
        # todo doc
        if int(type) == 1:
            return True

    def isDocumentationCategory(self, type: int) -> bool:
        # todo test
        # todo ref
        # todo doc
        if int(type) == 2:
            return True

    def isConfidentionalCategory(self, type: int) -> bool:
        # todo test
        # todo ref
        # todo doc
        if int(type) == 3:
            return True

    def getCategoriesSortedByType(self):
        # todo test
        # todo ref
        # todo doc
        # get file categories
        """
        Gets all catogries bby type. There are 3 types: public, documentation and confidential. returns:
        {
        {type:[{cat:{}}]}
        }
        :return:
        """

        publicCats = []
        documentCats = []
        confidentCats = []

        catList = self.getActiveCategoryListShort()
        for k, v in catList.items():
            catType = v['type']

            if self.isPublicCategory(catType):
                publicCats.append({k: v})
            if self.isDocumentationCategory(catType):
                documentCats.append({k: v})
            if self.isConfidentionalCategory(catType):
                confidentCats.append({k: v})

        return {category_types[0]: publicCats,
                category_types[1]: documentCats,
                category_types[2]: confidentCats
                }

    def getCategoryByType(self, type: str):
        # todo test
        # todo ref
        # todo doc
        """
        Print categories by given type
        [{22: {'short_description': 'Arbetsdagbok', 'description': 'Saker som rör kyrkan, sakristian i Hedemora',

        :param type:
        :return:
        """
        return self.getCategoriesSortedByType()[type]

    def printCategoriesByType(self):
        # todo test
        # todo ref
        # todo doc
        pubCatName = 'Public Categories'
        docCatName = 'Documentational Categories'
        confCatName = 'Confidentional Categories'
        for k, v in self.getCategoriesSortedByType().items():
            # print(f"{v}")
            if k == 'public':
                print(f"\n")
                print(f"{pubCatName} ({len(v)})")
                print(len(pubCatName) * '-')
                for it in v:
                    for cat, val in it.items():
                        print(f"{cat}: {val['short_description']}")

            if k == 'docs':
                print(f"\n")
                print(f"{docCatName} ({len(v)})")
                print(len(docCatName) * '-')
                for it in v:
                    for cat, val in it.items():
                        print(f"{cat}: {val['short_description']}")

            if k == 'conf':
                print(f"\n")
                print(f"{confCatName} ({len(v)})")
                print(len(confCatName) * '-')
                for it in v:
                    for cat, val in it.items():
                        print(f"{cat}: {val['short_description']}")


category = Category()

# zztest
#cat = Category().getActiveCategoryCount()
