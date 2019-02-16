resources = [
    {
        "name": "clinic",
        "keywords": ("clinic doctor's nurse practitioner office sick injury",),
        "phrase": ("a medical clinic",),
        "options": ("What kind of clinic are you needing?",),
        "children": (
            {
                "name": "urgent-care",
                "keywords": ("urgent-care urgent walk-in",),
                "phrase": ("an urgent-care clinic",),
                "children": [
                    {
                        "name": "northwest urgent-care",
                        "keywords": ("Northwest 412",),
                        "info": ({"name": "Northwest Urgent Care"},),
                        "isLeaf": True,
                        "phrase": ("Northwest Urgent Care",),
                    }
                ]
            },
            {
                "name": "primary-care",
                "keywords": ("primary-care primary care family-care family care family-practice",),
                "phrase": ("a primary-care clinic",),
                "children": [
                    {
                        "name": "community-clinic main",
                        "keywords": ("Community St.Francis",),
                        "info": ({"name": "Community Clinic on Holly Street"},),
                        "isLeaf": True,
                        "phrase": ("Community Clinic on Holly St.",),
                    }
                ]
            },
            {
                "name": "pediatric-care",
                "keywords": ("pediatrician pediatric child",),
                "phrase": ("a pediatric clinic",),
                "children": [
                    {
                        "name": "sager creek",
                        "keywords": ("Sager Creek",),
                        "info": ({"name": "Sager Creek on Progress Ave"},),
                        "isLeaf": True,
                        "phrase": ("Sager Creek",),
                    }
                ]
            },
        )
    },
    {
        "name": "food",
        "keywords": ("food meal hungry",),
        "phrase": ("a food pantry",),
        "options": ("What kind of food help do you need?",),
        "children": (
            {
                "name": "food pantry",
                "keywords": ("food pantry locker bank",),
                "phrase": ("a food pantry",),
                "children": [
                    {
                        "name": "Manna Center",
                        "keywords": ("Manna Center",),
                        "info": ({"address": "670 Heritage Ct.", "near": "The intersection of S. Carl and W. Tulsa"},),
                        "isLeaf": True,
                        "phrase": ("The Manna Center",),
                    },
                    {
                        "name": "Only Believe",
                        "keywords": ("Only Believe Tabernacle",),
                        "info": ({"name": "Only Believe Tabernacle"},),
                        "isLeaf": True,
                        "phrase": ("Only Believe Tabernacle",),
                    }
                ]
            },
        )
    }
]
