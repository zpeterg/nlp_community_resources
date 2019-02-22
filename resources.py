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
        "name": "suicide",
        "keywords": ("suicide kill die death slit",),
        "phrase": ("urgent help with thoughts of suicide or harm",),
        "children": (
            {
                "name": "911",
                "keywords": ("911 emergency",),
                "info": ({
                             "phone": "911",
                             "address": "603 N. Progress Ave",
                             "location": "ER across from Highschool"
                         },),
                "isLeaf": True,
                "phrase": ("emergency help",),
            },
            {
                "name": "Suicide Lifeline",
                "keywords": ("lifeline",),
                "info": ({
                             "phone": "800-273-8255",
                             "hours": "24/7",
                         },),
                "isLeaf": True,
                "phrase": ("suicide lifeline",),
            },
            {
                "name": "Crisis Hotline",
                "keywords": ("crisis hotline",),
                "info": ({
                             "phone": "888-274-7472",
                             "hours": "M-F 8am-1am, Sat-Sun 2pm-midnight",
                         },),
                "isLeaf": True,
                "phrase": ("crisis hotline",),
            },
        )
    },
    {
        "name": "mental health",
        "keywords": ("mental behavioral depression anxiety panic insane crazy nuts nervous breakdown",),
        "phrase": ("a mental health service",),
        "options": ("What kind of service are you needing?",),
        "children": (
            {
                "name": "counselor",
                "keywords": ("counselor behavioral",),
                "phrase": ("a counseling service",),
                "children": [
                    {
                        "name": "JBU Care Clinic",
                        "keywords": ("JBU",),
                        "info": ({
                            "phone": "479-524-7300",
                            "address": "2125 W. University Street",
                            "location": "Across from JBU"
                        },),
                        "isLeaf": True,
                        "phrase": ("1.JBU Care Clinic",),
                    },
                    {
                        "name": "Glenhaven Counseling",
                        "keywords": ("Glenhaven",),
                        "info": ({
                            "phone": "479-238-3950",
                            "address": "500 S. Broadway",
                            "location": "Across from Library"
                        },),
                        "isLeaf": True,
                        "phrase": ("2.Glenhaven Counseling",),
                    },
                    {
                        "name": "Ozark Guidance",
                        "keywords": ("OGC Ozark Guidance",),
                        "info": ({
                            "phone": "479-524-8618",
                            "address": "710 Holly Street",
                            "location": "Across from the Middle School"
                        },),
                        "isLeaf": True,
                        "phrase": ("3.Ozark Guidance",),
                    }
                ]
            },
            {
                "name": "psychiatrist",
                "keywords": ("psychiatry psychiatrist nurse-practitioner",),
                "phrase": ("a psychiatry service",),
                "children": [
                    {
                        "name": "Ozark Guidance",
                        "keywords": ("OGC Ozark Guidance",),
                        "info": ({
                            "phone": "479-524-8618",
                            "address": "710 Holly Street",
                            "location": "Across from the Middle School"
                        },),
                        "isLeaf": True,
                        "phrase": ("Ozark Guidance",),
                    }
                ]
            },
        )
    },
    {
        "name": "food",
        "keywords": ("food meal hungry",),
        "phrase": ("a food service",),
        "options": ("What kind of food help do you need?",),
        "children": (
            {
                "name": "food for children",
                "keywords": ("children",),
                "phrase": ("food for children",),
                "children": [
                    {
                        "name": "Summer Food Program",
                        "keywords": ("Manna Center",),
                        "info": ({
                            "Locations": "Allen Elementary 11-1, Bob Henry Park 11:30",
                            "Website": "http://www.fns.usda.gov/summerfoodrocks",
                        },),
                        "isLeaf": True,
                        "phrase": ("Summer Food Program",),
                    },
                ]
            },
            {
                "name": "food pantry",
                "keywords": ("pantry locker bank",),
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
    },
]
