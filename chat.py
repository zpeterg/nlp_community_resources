

class Chat:
    def __init__(self, resources, subject):
        self.resources = resources
        self.flattened = []
        self.subject = subject
        self.flatten()

    def flatten(self):
        rtn = []

        def loop(level, parent_names):
            for item in level:
                subject = parent_names + (item['name'],)
                new_item = {
                    "subject": subject,
                }
                if 'phrase' in item:
                    new_item['phrase'] = item['phrase']
                if 'options' in item:
                    new_item['options'] = item['options']
                if 'info' in item:
                    new_item['info'] = item['info']
                if 'isLeaf' in item:
                    new_item['isLeaf'] = item['isLeaf']
                # Add that item
                rtn.append(new_item)
                # Move into the children and loop them
                if 'children' in item:
                    loop(item['children'], subject)

        loop(self.resources, ())
        self.flattened = rtn

    def match(self, searchStr):
        print('subject------', self.subject)
        sub_resource = next(i for i in self.flattened if ''.join(i['subject']) == ''.join(self.subject))
        ################### todo: add the search within sub_resources using searchStr and parsePhrase()
        return sub_resource
