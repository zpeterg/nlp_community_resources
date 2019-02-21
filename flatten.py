def flatten(resources, language):
    rtn = []

    def loop(level, parent_names, parent_keywords):
        for item in level:
            subject = parent_names + (item['name'],)
            keywords = parent_keywords + (item['keywords'][language],)
            new_item = {
                "subject": subject,
                "keywords": keywords,
            }
            if 'phrase' in item:
                new_item['phrase'] = item['phrase']
            if 'options' in item:
                new_item['options'] = item['options']
            if 'info' in item:
                new_item['info'] = item['info']
            if 'isLeaf' in item:
                new_item['isLeaf'] = item['isLeaf']
            if 'children' in item:
                children = ()
                for c in item['children']:
                    children += (c['phrase'][language],)
                new_item['children'] = children
            # Add that item
            rtn.append(new_item)
            # Move into the children and loop them
            if 'children' in item:
                loop(item['children'], subject, keywords)

    loop(resources, (), ())
    return rtn
