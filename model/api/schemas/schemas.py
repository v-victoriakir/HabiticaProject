post_auth_successful = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "data": {
            "type": "object",
            "properties": {
                "auth": {
                    "type": "object",
                    "properties": {
                        "local": {
                            "type": "object",
                            "properties": {
                                "email": {
                                    "type": "string"
                                },
                                "username": {
                                    "type": "string"
                                },
                                "lowerCaseUsername": {
                                    "type": "string"
                                },
                                "has_password": {
                                    "type": "boolean"
                                }
                            },
                            "required": [
                                "email",
                                "username",
                                "lowerCaseUsername",
                                "has_password"
                            ]
                        },
                        "timestamps": {
                            "type": "object",
                            "properties": {
                                "created": {
                                    "type": "string"
                                },
                                "loggedin": {
                                    "type": "string"
                                },
                                "updated": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "created",
                                "loggedin",
                                "updated"
                            ]
                        },
                        "facebook": {
                            "type": "object"
                        },
                        "google": {
                            "type": "object"
                        },
                        "apple": {
                            "type": "object"
                        }
                    },
                    "required": [
                        "local",
                        "timestamps",
                        "facebook",
                        "google",
                        "apple"
                    ]
                },
                "achievements": {
                    "type": "object",
                    "properties": {
                        "ultimateGearSets": {
                            "type": "object",
                            "properties": {
                                "healer": {
                                    "type": "boolean"
                                },
                                "wizard": {
                                    "type": "boolean"
                                },
                                "rogue": {
                                    "type": "boolean"
                                },
                                "warrior": {
                                    "type": "boolean"
                                }
                            },
                            "required": [
                                "healer",
                                "wizard",
                                "rogue",
                                "warrior"
                            ]
                        },
                        "streak": {
                            "type": "integer"
                        },
                        "challenges": {
                            "type": "array",
                            "items": {}
                        },
                        "perfect": {
                            "type": "integer"
                        },
                        "quests": {
                            "type": "object"
                        },
                        "createdTask": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "ultimateGearSets",
                        "streak",
                        "challenges",
                        "perfect",
                        "quests",
                        "createdTask"
                    ]
                },
                "backer": {
                    "type": "object"
                },
                "contributor": {
                    "type": "object"
                },
                "permissions": {
                    "type": "object"
                },
                "purchased": {
                    "type": "object",
                    "properties": {
                        "ads": {
                            "type": "boolean"
                        },
                        "txnCount": {
                            "type": "integer"
                        },
                        "skin": {
                            "type": "object"
                        },
                        "hair": {
                            "type": "object"
                        },
                        "shirt": {
                            "type": "object"
                        },
                        "background": {
                            "type": "object",
                            "properties": {
                                "violet": {
                                    "type": "boolean"
                                },
                                "blue": {
                                    "type": "boolean"
                                },
                                "green": {
                                    "type": "boolean"
                                },
                                "purple": {
                                    "type": "boolean"
                                },
                                "red": {
                                    "type": "boolean"
                                },
                                "yellow": {
                                    "type": "boolean"
                                }
                            },
                            "required": [
                                "violet",
                                "blue",
                                "green",
                                "purple",
                                "red",
                                "yellow"
                            ]
                        },
                        "plan": {
                            "type": "object",
                            "properties": {
                                "consecutive": {
                                    "type": "object",
                                    "properties": {
                                        "count": {
                                            "type": "integer"
                                        },
                                        "offset": {
                                            "type": "integer"
                                        },
                                        "gemCapExtra": {
                                            "type": "integer"
                                        },
                                        "trinkets": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "count",
                                        "offset",
                                        "gemCapExtra",
                                        "trinkets"
                                    ]
                                },
                                "quantity": {
                                    "type": "integer"
                                },
                                "extraMonths": {
                                    "type": "integer"
                                },
                                "gemsBought": {
                                    "type": "integer"
                                },
                                "cumulativeCount": {
                                    "type": "integer"
                                },
                                "mysteryItems": {
                                    "type": "array",
                                    "items": {}
                                },
                                "dateUpdated": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "consecutive",
                                "quantity",
                                "extraMonths",
                                "gemsBought",
                                "cumulativeCount",
                                "mysteryItems",
                                "dateUpdated"
                            ]
                        }
                    },
                    "required": [
                        "ads",
                        "txnCount",
                        "skin",
                        "hair",
                        "shirt",
                        "background",
                        "plan"
                    ]
                },
                "flags": {
                    "type": "object",
                    "properties": {
                        "tour": {
                            "type": "object",
                            "properties": {
                                "intro": {
                                    "type": "integer"
                                },
                                "classes": {
                                    "type": "integer"
                                },
                                "stats": {
                                    "type": "integer"
                                },
                                "tavern": {
                                    "type": "integer"
                                },
                                "party": {
                                    "type": "integer"
                                },
                                "guilds": {
                                    "type": "integer"
                                },
                                "challenges": {
                                    "type": "integer"
                                },
                                "market": {
                                    "type": "integer"
                                },
                                "pets": {
                                    "type": "integer"
                                },
                                "mounts": {
                                    "type": "integer"
                                },
                                "hall": {
                                    "type": "integer"
                                },
                                "equipment": {
                                    "type": "integer"
                                },
                                "groupPlans": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "intro",
                                "classes",
                                "stats",
                                "tavern",
                                "party",
                                "guilds",
                                "challenges",
                                "market",
                                "pets",
                                "mounts",
                                "hall",
                                "equipment",
                                "groupPlans"
                            ]
                        },
                        "tutorial": {
                            "type": "object",
                            "properties": {
                                "common": {
                                    "type": "object",
                                    "properties": {
                                        "habits": {
                                            "type": "boolean"
                                        },
                                        "dailies": {
                                            "type": "boolean"
                                        },
                                        "todos": {
                                            "type": "boolean"
                                        },
                                        "rewards": {
                                            "type": "boolean"
                                        },
                                        "party": {
                                            "type": "boolean"
                                        },
                                        "pets": {
                                            "type": "boolean"
                                        },
                                        "gems": {
                                            "type": "boolean"
                                        },
                                        "skills": {
                                            "type": "boolean"
                                        },
                                        "classes": {
                                            "type": "boolean"
                                        },
                                        "tavern": {
                                            "type": "boolean"
                                        },
                                        "equipment": {
                                            "type": "boolean"
                                        },
                                        "items": {
                                            "type": "boolean"
                                        },
                                        "mounts": {
                                            "type": "boolean"
                                        },
                                        "inbox": {
                                            "type": "boolean"
                                        },
                                        "stats": {
                                            "type": "boolean"
                                        }
                                    },
                                    "required": [
                                        "habits",
                                        "dailies",
                                        "todos",
                                        "rewards",
                                        "party",
                                        "pets",
                                        "gems",
                                        "skills",
                                        "classes",
                                        "tavern",
                                        "equipment",
                                        "items",
                                        "mounts",
                                        "inbox",
                                        "stats"
                                    ]
                                },
                                "ios": {
                                    "type": "object",
                                    "properties": {
                                        "addTask": {
                                            "type": "boolean"
                                        },
                                        "editTask": {
                                            "type": "boolean"
                                        },
                                        "deleteTask": {
                                            "type": "boolean"
                                        },
                                        "filterTask": {
                                            "type": "boolean"
                                        },
                                        "groupPets": {
                                            "type": "boolean"
                                        },
                                        "inviteParty": {
                                            "type": "boolean"
                                        },
                                        "reorderTask": {
                                            "type": "boolean"
                                        }
                                    },
                                    "required": [
                                        "addTask",
                                        "editTask",
                                        "deleteTask",
                                        "filterTask",
                                        "groupPets",
                                        "inviteParty",
                                        "reorderTask"
                                    ]
                                }
                            },
                            "required": [
                                "common",
                                "ios"
                            ]
                        },
                        "verifiedUsername": {
                            "type": "boolean"
                        },
                        "customizationsNotification": {
                            "type": "boolean"
                        },
                        "showTour": {
                            "type": "boolean"
                        },
                        "dropsEnabled": {
                            "type": "boolean"
                        },
                        "itemsEnabled": {
                            "type": "boolean"
                        },
                        "lastNewStuffRead": {
                            "type": "string"
                        },
                        "rewrite": {
                            "type": "boolean"
                        },
                        "classSelected": {
                            "type": "boolean"
                        },
                        "rebirthEnabled": {
                            "type": "boolean"
                        },
                        "levelDrops": {
                            "type": "object"
                        },
                        "recaptureEmailsPhase": {
                            "type": "integer"
                        },
                        "weeklyRecapEmailsPhase": {
                            "type": "integer"
                        },
                        "lastWeeklyRecap": {
                            "type": "string"
                        },
                        "communityGuidelinesAccepted": {
                            "type": "boolean"
                        },
                        "cronCount": {
                            "type": "integer"
                        },
                        "welcomed": {
                            "type": "boolean"
                        },
                        "armoireEnabled": {
                            "type": "boolean"
                        },
                        "armoireOpened": {
                            "type": "boolean"
                        },
                        "armoireEmpty": {
                            "type": "boolean"
                        },
                        "cardReceived": {
                            "type": "boolean"
                        },
                        "warnedLowHealth": {
                            "type": "boolean"
                        },
                        "initializedUserHistory": {
                            "type": "boolean"
                        },
                        "thirdPartyTools": {
                            "type": "string"
                        },
                        "newStuff": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "tour",
                        "tutorial",
                        "verifiedUsername",
                        "customizationsNotification",
                        "showTour",
                        "dropsEnabled",
                        "itemsEnabled",
                        "lastNewStuffRead",
                        "rewrite",
                        "classSelected",
                        "rebirthEnabled",
                        "levelDrops",
                        "recaptureEmailsPhase",
                        "weeklyRecapEmailsPhase",
                        "lastWeeklyRecap",
                        "communityGuidelinesAccepted",
                        "cronCount",
                        "welcomed",
                        "armoireEnabled",
                        "armoireOpened",
                        "armoireEmpty",
                        "cardReceived",
                        "warnedLowHealth",
                        "initializedUserHistory",
                        "thirdPartyTools",
                        "newStuff"
                    ]
                },
                "history": {
                    "type": "object",
                    "properties": {
                        "exp": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "date": {
                                            "type": "string"
                                        },
                                        "value": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "date",
                                        "value"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "date": {
                                            "type": "string"
                                        },
                                        "value": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "date",
                                        "value"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "date": {
                                            "type": "string"
                                        },
                                        "value": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "date",
                                        "value"
                                    ]
                                }
                            ]
                        },
                        "todos": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "date": {
                                            "type": "string"
                                        },
                                        "value": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "date",
                                        "value"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "date": {
                                            "type": "string"
                                        },
                                        "value": {
                                            "type": "number"
                                        }
                                    },
                                    "required": [
                                        "date",
                                        "value"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "date": {
                                            "type": "string"
                                        },
                                        "value": {
                                            "type": "number"
                                        }
                                    },
                                    "required": [
                                        "date",
                                        "value"
                                    ]
                                }
                            ]
                        }
                    },
                    "required": [
                        "exp",
                        "todos"
                    ]
                },
                "items": {
                    "type": "object",
                    "properties": {
                        "gear": {
                            "type": "object",
                            "properties": {
                                "equipped": {
                                    "type": "object",
                                    "properties": {
                                        "armor": {
                                            "type": "string"
                                        },
                                        "head": {
                                            "type": "string"
                                        },
                                        "shield": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "armor",
                                        "head",
                                        "shield"
                                    ]
                                },
                                "costume": {
                                    "type": "object",
                                    "properties": {
                                        "armor": {
                                            "type": "string"
                                        },
                                        "head": {
                                            "type": "string"
                                        },
                                        "shield": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "armor",
                                        "head",
                                        "shield"
                                    ]
                                },
                                "owned": {
                                    "type": "object",
                                    "properties": {
                                        "headAccessory_special_blackHeadband": {
                                            "type": "boolean"
                                        },
                                        "headAccessory_special_blueHeadband": {
                                            "type": "boolean"
                                        },
                                        "headAccessory_special_greenHeadband": {
                                            "type": "boolean"
                                        },
                                        "headAccessory_special_pinkHeadband": {
                                            "type": "boolean"
                                        },
                                        "headAccessory_special_redHeadband": {
                                            "type": "boolean"
                                        },
                                        "headAccessory_special_whiteHeadband": {
                                            "type": "boolean"
                                        },
                                        "headAccessory_special_yellowHeadband": {
                                            "type": "boolean"
                                        },
                                        "eyewear_special_blackTopFrame": {
                                            "type": "boolean"
                                        },
                                        "eyewear_special_blueTopFrame": {
                                            "type": "boolean"
                                        },
                                        "eyewear_special_greenTopFrame": {
                                            "type": "boolean"
                                        },
                                        "eyewear_special_pinkTopFrame": {
                                            "type": "boolean"
                                        },
                                        "eyewear_special_redTopFrame": {
                                            "type": "boolean"
                                        },
                                        "eyewear_special_whiteTopFrame": {
                                            "type": "boolean"
                                        },
                                        "eyewear_special_yellowTopFrame": {
                                            "type": "boolean"
                                        },
                                        "eyewear_special_blackHalfMoon": {
                                            "type": "boolean"
                                        },
                                        "eyewear_special_blueHalfMoon": {
                                            "type": "boolean"
                                        },
                                        "eyewear_special_greenHalfMoon": {
                                            "type": "boolean"
                                        },
                                        "eyewear_special_pinkHalfMoon": {
                                            "type": "boolean"
                                        },
                                        "eyewear_special_redHalfMoon": {
                                            "type": "boolean"
                                        },
                                        "eyewear_special_whiteHalfMoon": {
                                            "type": "boolean"
                                        },
                                        "eyewear_special_yellowHalfMoon": {
                                            "type": "boolean"
                                        },
                                        "armor_special_bardRobes": {
                                            "type": "boolean"
                                        },
                                        "head_special_bardHat": {
                                            "type": "boolean"
                                        }
                                    },
                                    "required": [
                                        "headAccessory_special_blackHeadband",
                                        "headAccessory_special_blueHeadband",
                                        "headAccessory_special_greenHeadband",
                                        "headAccessory_special_pinkHeadband",
                                        "headAccessory_special_redHeadband",
                                        "headAccessory_special_whiteHeadband",
                                        "headAccessory_special_yellowHeadband",
                                        "eyewear_special_blackTopFrame",
                                        "eyewear_special_blueTopFrame",
                                        "eyewear_special_greenTopFrame",
                                        "eyewear_special_pinkTopFrame",
                                        "eyewear_special_redTopFrame",
                                        "eyewear_special_whiteTopFrame",
                                        "eyewear_special_yellowTopFrame",
                                        "eyewear_special_blackHalfMoon",
                                        "eyewear_special_blueHalfMoon",
                                        "eyewear_special_greenHalfMoon",
                                        "eyewear_special_pinkHalfMoon",
                                        "eyewear_special_redHalfMoon",
                                        "eyewear_special_whiteHalfMoon",
                                        "eyewear_special_yellowHalfMoon",
                                        "armor_special_bardRobes",
                                        "head_special_bardHat"
                                    ]
                                }
                            },
                            "required": [
                                "equipped",
                                "costume",
                                "owned"
                            ]
                        },
                        "special": {
                            "type": "object",
                            "properties": {
                                "snowball": {
                                    "type": "integer"
                                },
                                "spookySparkles": {
                                    "type": "integer"
                                },
                                "shinySeed": {
                                    "type": "integer"
                                },
                                "seafoam": {
                                    "type": "integer"
                                },
                                "valentine": {
                                    "type": "integer"
                                },
                                "valentineReceived": {
                                    "type": "array",
                                    "items": {}
                                },
                                "nye": {
                                    "type": "integer"
                                },
                                "nyeReceived": {
                                    "type": "array",
                                    "items": {}
                                },
                                "greeting": {
                                    "type": "integer"
                                },
                                "greetingReceived": {
                                    "type": "array",
                                    "items": {}
                                },
                                "thankyou": {
                                    "type": "integer"
                                },
                                "thankyouReceived": {
                                    "type": "array",
                                    "items": {}
                                },
                                "birthday": {
                                    "type": "integer"
                                },
                                "birthdayReceived": {
                                    "type": "array",
                                    "items": {}
                                },
                                "congrats": {
                                    "type": "integer"
                                },
                                "congratsReceived": {
                                    "type": "array",
                                    "items": {}
                                },
                                "getwell": {
                                    "type": "integer"
                                },
                                "getwellReceived": {
                                    "type": "array",
                                    "items": {}
                                },
                                "goodluck": {
                                    "type": "integer"
                                },
                                "goodluckReceived": {
                                    "type": "array",
                                    "items": {}
                                }
                            },
                            "required": [
                                "snowball",
                                "spookySparkles",
                                "shinySeed",
                                "seafoam",
                                "valentine",
                                "valentineReceived",
                                "nye",
                                "nyeReceived",
                                "greeting",
                                "greetingReceived",
                                "thankyou",
                                "thankyouReceived",
                                "birthday",
                                "birthdayReceived",
                                "congrats",
                                "congratsReceived",
                                "getwell",
                                "getwellReceived",
                                "goodluck",
                                "goodluckReceived"
                            ]
                        },
                        "lastDrop": {
                            "type": "object",
                            "properties": {
                                "count": {
                                    "type": "integer"
                                },
                                "date": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "count",
                                "date"
                            ]
                        },
                        "currentPet": {
                            "type": "string"
                        },
                        "currentMount": {
                            "type": "string"
                        },
                        "pets": {
                            "type": "object"
                        },
                        "eggs": {
                            "type": "object"
                        },
                        "hatchingPotions": {
                            "type": "object"
                        },
                        "food": {
                            "type": "object"
                        },
                        "mounts": {
                            "type": "object",
                            "properties": {
                                "Orca-Base": {
                                    "type": "boolean"
                                }
                            },
                            "required": [
                                "Orca-Base"
                            ]
                        },
                        "quests": {
                            "type": "object",
                            "properties": {
                                "dustbunnies": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "dustbunnies"
                            ]
                        }
                    },
                    "required": [
                        "gear",
                        "special",
                        "lastDrop",
                        "currentPet",
                        "currentMount",
                        "pets",
                        "eggs",
                        "hatchingPotions",
                        "food",
                        "mounts",
                        "quests"
                    ]
                },
                "invitations": {
                    "type": "object",
                    "properties": {
                        "guilds": {
                            "type": "array",
                            "items": {}
                        },
                        "party": {
                            "type": "object"
                        },
                        "parties": {
                            "type": "array",
                            "items": {}
                        }
                    },
                    "required": [
                        "guilds",
                        "party",
                        "parties"
                    ]
                },
                "party": {
                    "type": "object",
                    "properties": {
                        "quest": {
                            "type": "object",
                            "properties": {
                                "progress": {
                                    "type": "object",
                                    "properties": {
                                        "up": {
                                            "type": "integer"
                                        },
                                        "down": {
                                            "type": "integer"
                                        },
                                        "collectedItems": {
                                            "type": "integer"
                                        },
                                        "collect": {
                                            "type": "object"
                                        }
                                    },
                                    "required": [
                                        "up",
                                        "down",
                                        "collectedItems",
                                        "collect"
                                    ]
                                },
                                "RSVPNeeded": {
                                    "type": "boolean"
                                }
                            },
                            "required": [
                                "progress",
                                "RSVPNeeded"
                            ]
                        },
                        "order": {
                            "type": "string"
                        },
                        "orderAscending": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "quest",
                        "order",
                        "orderAscending"
                    ]
                },
                "preferences": {
                    "type": "object",
                    "properties": {
                        "hair": {
                            "type": "object",
                            "properties": {
                                "color": {
                                    "type": "string"
                                },
                                "base": {
                                    "type": "integer"
                                },
                                "bangs": {
                                    "type": "integer"
                                },
                                "beard": {
                                    "type": "integer"
                                },
                                "mustache": {
                                    "type": "integer"
                                },
                                "flower": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "color",
                                "base",
                                "bangs",
                                "beard",
                                "mustache",
                                "flower"
                            ]
                        },
                        "emailNotifications": {
                            "type": "object",
                            "properties": {
                                "unsubscribeFromAll": {
                                    "type": "boolean"
                                },
                                "newPM": {
                                    "type": "boolean"
                                },
                                "kickedGroup": {
                                    "type": "boolean"
                                },
                                "wonChallenge": {
                                    "type": "boolean"
                                },
                                "giftedGems": {
                                    "type": "boolean"
                                },
                                "giftedSubscription": {
                                    "type": "boolean"
                                },
                                "invitedParty": {
                                    "type": "boolean"
                                },
                                "invitedGuild": {
                                    "type": "boolean"
                                },
                                "questStarted": {
                                    "type": "boolean"
                                },
                                "invitedQuest": {
                                    "type": "boolean"
                                },
                                "importantAnnouncements": {
                                    "type": "boolean"
                                },
                                "weeklyRecaps": {
                                    "type": "boolean"
                                },
                                "onboarding": {
                                    "type": "boolean"
                                },
                                "majorUpdates": {
                                    "type": "boolean"
                                },
                                "subscriptionReminders": {
                                    "type": "boolean"
                                },
                                "contentRelease": {
                                    "type": "boolean"
                                }
                            },
                            "required": [
                                "unsubscribeFromAll",
                                "newPM",
                                "kickedGroup",
                                "wonChallenge",
                                "giftedGems",
                                "giftedSubscription",
                                "invitedParty",
                                "invitedGuild",
                                "questStarted",
                                "invitedQuest",
                                "importantAnnouncements",
                                "weeklyRecaps",
                                "onboarding",
                                "majorUpdates",
                                "subscriptionReminders",
                                "contentRelease"
                            ]
                        },
                        "pushNotifications": {
                            "type": "object",
                            "properties": {
                                "unsubscribeFromAll": {
                                    "type": "boolean"
                                },
                                "newPM": {
                                    "type": "boolean"
                                },
                                "wonChallenge": {
                                    "type": "boolean"
                                },
                                "giftedGems": {
                                    "type": "boolean"
                                },
                                "giftedSubscription": {
                                    "type": "boolean"
                                },
                                "invitedParty": {
                                    "type": "boolean"
                                },
                                "invitedGuild": {
                                    "type": "boolean"
                                },
                                "questStarted": {
                                    "type": "boolean"
                                },
                                "invitedQuest": {
                                    "type": "boolean"
                                },
                                "majorUpdates": {
                                    "type": "boolean"
                                },
                                "mentionParty": {
                                    "type": "boolean"
                                },
                                "mentionJoinedGuild": {
                                    "type": "boolean"
                                },
                                "mentionUnjoinedGuild": {
                                    "type": "boolean"
                                },
                                "partyActivity": {
                                    "type": "boolean"
                                },
                                "contentRelease": {
                                    "type": "boolean"
                                }
                            },
                            "required": [
                                "unsubscribeFromAll",
                                "newPM",
                                "wonChallenge",
                                "giftedGems",
                                "giftedSubscription",
                                "invitedParty",
                                "invitedGuild",
                                "questStarted",
                                "invitedQuest",
                                "majorUpdates",
                                "mentionParty",
                                "mentionJoinedGuild",
                                "mentionUnjoinedGuild",
                                "partyActivity",
                                "contentRelease"
                            ]
                        },
                        "suppressModals": {
                            "type": "object",
                            "properties": {
                                "levelUp": {
                                    "type": "boolean"
                                },
                                "hatchPet": {
                                    "type": "boolean"
                                },
                                "raisePet": {
                                    "type": "boolean"
                                },
                                "streak": {
                                    "type": "boolean"
                                }
                            },
                            "required": [
                                "levelUp",
                                "hatchPet",
                                "raisePet",
                                "streak"
                            ]
                        },
                        "tasks": {
                            "type": "object",
                            "properties": {
                                "activeFilter": {
                                    "type": "object",
                                    "properties": {
                                        "habit": {
                                            "type": "string"
                                        },
                                        "daily": {
                                            "type": "string"
                                        },
                                        "todo": {
                                            "type": "string"
                                        },
                                        "reward": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "habit",
                                        "daily",
                                        "todo",
                                        "reward"
                                    ]
                                },
                                "groupByChallenge": {
                                    "type": "boolean"
                                },
                                "confirmScoreNotes": {
                                    "type": "boolean"
                                },
                                "mirrorGroupTasks": {
                                    "type": "array",
                                    "items": {}
                                }
                            },
                            "required": [
                                "activeFilter",
                                "groupByChallenge",
                                "confirmScoreNotes",
                                "mirrorGroupTasks"
                            ]
                        },
                        "language": {
                            "type": "string"
                        },
                        "dayStart": {
                            "type": "integer"
                        },
                        "size": {
                            "type": "string"
                        },
                        "hideHeader": {
                            "type": "boolean"
                        },
                        "skin": {
                            "type": "string"
                        },
                        "shirt": {
                            "type": "string"
                        },
                        "timezoneOffset": {
                            "type": "integer"
                        },
                        "sound": {
                            "type": "string"
                        },
                        "chair": {
                            "type": "string"
                        },
                        "allocationMode": {
                            "type": "string"
                        },
                        "autoEquip": {
                            "type": "boolean"
                        },
                        "costume": {
                            "type": "boolean"
                        },
                        "dateFormat": {
                            "type": "string"
                        },
                        "sleep": {
                            "type": "boolean"
                        },
                        "stickyHeader": {
                            "type": "boolean"
                        },
                        "disableClasses": {
                            "type": "boolean"
                        },
                        "newTaskEdit": {
                            "type": "boolean"
                        },
                        "dailyDueDefaultView": {
                            "type": "boolean"
                        },
                        "advancedCollapsed": {
                            "type": "boolean"
                        },
                        "toolbarCollapsed": {
                            "type": "boolean"
                        },
                        "reverseChatOrder": {
                            "type": "boolean"
                        },
                        "developerMode": {
                            "type": "boolean"
                        },
                        "displayInviteToPartyWhenPartyIs1": {
                            "type": "boolean"
                        },
                        "webhooks": {
                            "type": "object"
                        },
                        "improvementCategories": {
                            "type": "array",
                            "items": {}
                        },
                        "background": {
                            "type": "string"
                        },
                        "timezoneOffsetAtLastCron": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "hair",
                        "emailNotifications",
                        "pushNotifications",
                        "suppressModals",
                        "tasks",
                        "language",
                        "dayStart",
                        "size",
                        "hideHeader",
                        "skin",
                        "shirt",
                        "timezoneOffset",
                        "sound",
                        "chair",
                        "allocationMode",
                        "autoEquip",
                        "costume",
                        "dateFormat",
                        "sleep",
                        "stickyHeader",
                        "disableClasses",
                        "newTaskEdit",
                        "dailyDueDefaultView",
                        "advancedCollapsed",
                        "toolbarCollapsed",
                        "reverseChatOrder",
                        "developerMode",
                        "displayInviteToPartyWhenPartyIs1",
                        "webhooks",
                        "improvementCategories",
                        "background",
                        "timezoneOffsetAtLastCron"
                    ]
                },
                "profile": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "blurb": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "name",
                        "blurb"
                    ]
                },
                "stats": {
                    "type": "object",
                    "properties": {
                        "buffs": {
                            "type": "object",
                            "properties": {
                                "str": {
                                    "type": "integer"
                                },
                                "int": {
                                    "type": "integer"
                                },
                                "per": {
                                    "type": "integer"
                                },
                                "con": {
                                    "type": "integer"
                                },
                                "stealth": {
                                    "type": "integer"
                                },
                                "streaks": {
                                    "type": "boolean"
                                },
                                "seafoam": {
                                    "type": "boolean"
                                },
                                "shinySeed": {
                                    "type": "boolean"
                                },
                                "snowball": {
                                    "type": "boolean"
                                },
                                "spookySparkles": {
                                    "type": "boolean"
                                }
                            },
                            "required": [
                                "str",
                                "int",
                                "per",
                                "con",
                                "stealth",
                                "streaks",
                                "seafoam",
                                "shinySeed",
                                "snowball",
                                "spookySparkles"
                            ]
                        },
                        "training": {
                            "type": "object",
                            "properties": {
                                "int": {
                                    "type": "integer"
                                },
                                "per": {
                                    "type": "integer"
                                },
                                "str": {
                                    "type": "integer"
                                },
                                "con": {
                                    "type": "integer"
                                }
                            },
                            "required": [
                                "int",
                                "per",
                                "str",
                                "con"
                            ]
                        },
                        "hp": {
                            "type": "number"
                        },
                        "mp": {
                            "type": "number"
                        },
                        "exp": {
                            "type": "integer"
                        },
                        "gp": {
                            "type": "integer"
                        },
                        "lvl": {
                            "type": "integer"
                        },
                        "class": {
                            "type": "string"
                        },
                        "points": {
                            "type": "integer"
                        },
                        "str": {
                            "type": "integer"
                        },
                        "con": {
                            "type": "integer"
                        },
                        "int": {
                            "type": "integer"
                        },
                        "per": {
                            "type": "integer"
                        },
                        "toNextLevel": {
                            "type": "integer"
                        },
                        "maxHealth": {
                            "type": "integer"
                        },
                        "maxMP": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "buffs",
                        "training",
                        "hp",
                        "mp",
                        "exp",
                        "gp",
                        "lvl",
                        "class",
                        "points",
                        "str",
                        "con",
                        "int",
                        "per",
                        "toNextLevel",
                        "maxHealth",
                        "maxMP"
                    ]
                },
                "inbox": {
                    "type": "object",
                    "properties": {
                        "newMessages": {
                            "type": "integer"
                        },
                        "optOut": {
                            "type": "boolean"
                        },
                        "blocks": {
                            "type": "array",
                            "items": {}
                        }
                    },
                    "required": [
                        "newMessages",
                        "optOut",
                        "blocks"
                    ]
                },
                "tasksOrder": {
                    "type": "object",
                    "properties": {
                        "habits": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                }
                            ]
                        },
                        "dailys": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                }
                            ]
                        },
                        "todos": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                }
                            ]
                        },
                        "rewards": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                }
                            ]
                        }
                    },
                    "required": [
                        "habits",
                        "dailys",
                        "todos",
                        "rewards"
                    ]
                },
                "_id": {
                    "type": "string"
                },
                "_v": {
                    "type": "integer"
                },
                "balance": {
                    "type": "number"
                },
                "_subSignature": {
                    "type": "string"
                },
                "challenges": {
                    "type": "array",
                    "items": {}
                },
                "guilds": {
                    "type": "array",
                    "items": {}
                },
                "loginIncentives": {
                    "type": "integer"
                },
                "invitesSent": {
                    "type": "integer"
                },
                "pinnedItemsOrder": {
                    "type": "array",
                    "items": {}
                },
                "lastCron": {
                    "type": "string"
                },
                "newMessages": {
                    "type": "object"
                },
                "notifications": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string"
                                },
                                "data": {
                                    "type": "object",
                                    "properties": {
                                        "icon": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "text": {
                                            "type": "string"
                                        },
                                        "destination": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "icon",
                                        "title",
                                        "text",
                                        "destination"
                                    ]
                                },
                                "seen": {
                                    "type": "boolean"
                                },
                                "id": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "type",
                                "data",
                                "seen",
                                "id"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string"
                                },
                                "data": {
                                    "type": "object",
                                    "properties": {
                                        "title": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "title"
                                    ]
                                },
                                "seen": {
                                    "type": "boolean"
                                },
                                "id": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "type",
                                "data",
                                "seen",
                                "id"
                            ]
                        }
                    ]
                },
                "tags": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "id",
                                "name"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "id",
                                "name"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "id",
                                "name"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "id",
                                "name"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "id",
                                "name"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "id",
                                "name"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "id",
                                "name"
                            ]
                        }
                    ]
                },
                "extra": {
                    "type": "object"
                },
                "pushDevices": {
                    "type": "array",
                    "items": {}
                },
                "webhooks": {
                    "type": "array",
                    "items": {}
                },
                "pinnedItems": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "path": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "path",
                                "type"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "path": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "path",
                                "type"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "path": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "path",
                                "type"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "path": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "path",
                                "type"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "path": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "path",
                                "type"
                            ]
                        },
                        {
                            "type": "object",
                            "properties": {
                                "path": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "path",
                                "type"
                            ]
                        }
                    ]
                },
                "unpinnedItems": {
                    "type": "array",
                    "items": {}
                },
                "migration": {
                    "type": "string"
                },
                "id": {
                    "type": "string"
                },
                "needsCron": {
                    "type": "boolean"
                }
            },
            "required": [
                "auth",
                "achievements",
                "backer",
                "contributor",
                "permissions",
                "purchased",
                "flags",
                "history",
                "items",
                "invitations",
                "party",
                "preferences",
                "profile",
                "stats",
                "inbox",
                "tasksOrder",
                "_id",
                "_v",
                "balance",
                "_subSignature",
                "challenges",
                "guilds",
                "loginIncentives",
                "invitesSent",
                "pinnedItemsOrder",
                "lastCron",
                "newMessages",
                "notifications",
                "tags",
                "extra",
                "pushDevices",
                "webhooks",
                "pinnedItems",
                "unpinnedItems",
                "migration",
                "id",
                "needsCron"
            ]
        },
        "notifications": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "data": {
                            "type": "object",
                            "properties": {
                                "icon": {
                                    "type": "string"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "text": {
                                    "type": "string"
                                },
                                "destination": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "icon",
                                "title",
                                "text",
                                "destination"
                            ]
                        },
                        "seen": {
                            "type": "boolean"
                        },
                        "id": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "data",
                        "seen",
                        "id"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "data": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "title"
                            ]
                        },
                        "seen": {
                            "type": "boolean"
                        },
                        "id": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "data",
                        "seen",
                        "id"
                    ]
                }
            ]
        },
        "userV": {
            "type": "integer"
        },
        "appVersion": {
            "type": "string"
        }
    },
    "required": [
        "success",
        "data",
        "notifications",
        "userV",
        "appVersion"
    ]
}

post_auth_unsuccessful = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "error": {
            "type": "string"
        },
        "message": {
            "type": "string"
        }
    },
    "required": [
        "success",
        "error",
        "message"
    ]
}

post_create_task = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "data": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string"
                },
                "text": {
                    "type": "string"
                },
                "notes": {
                    "type": "string"
                },
                "tags": {
                    "type": "array",
                    "items": {}
                },
                "value": {
                    "type": "integer"
                },
                "priority": {
                    "type": "integer"
                },
                "attribute": {
                    "type": "string"
                },
                "challenge": {
                    "type": "object"
                },
                "group": {
                    "type": "object",
                    "properties": {
                        "completedBy": {
                            "type": "object"
                        },
                        "assignedUsers": {
                            "type": "array",
                            "items": {}
                        }
                    },
                    "required": [
                        "completedBy",
                        "assignedUsers"
                    ]
                },
                "reminders": {
                    "type": "array",
                    "items": {}
                },
                "byHabitica": {
                    "type": "boolean"
                },
                "_id": {
                    "type": "string"
                },
                "frequency": {
                    "type": "string"
                },
                "everyX": {
                    "type": "integer"
                },
                "startDate": {
                    "type": "string"
                },
                "repeat": {
                    "type": "object",
                    "properties": {
                        "m": {
                            "type": "boolean"
                        },
                        "t": {
                            "type": "boolean"
                        },
                        "w": {
                            "type": "boolean"
                        },
                        "th": {
                            "type": "boolean"
                        },
                        "f": {
                            "type": "boolean"
                        },
                        "s": {
                            "type": "boolean"
                        },
                        "su": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "m",
                        "t",
                        "w",
                        "th",
                        "f",
                        "s",
                        "su"
                    ]
                },
                "streak": {
                    "type": "integer"
                },
                "daysOfMonth": {
                    "type": "array",
                    "items": {}
                },
                "weeksOfMonth": {
                    "type": "array",
                    "items": {}
                },
                "nextDue": {
                    "type": "array",
                    "items": [
                        {
                            "type": "string"
                        },
                        {
                            "type": "string"
                        },
                        {
                            "type": "string"
                        },
                        {
                            "type": "string"
                        },
                        {
                            "type": "string"
                        },
                        {
                            "type": "string"
                        }
                    ]
                },
                "yesterDaily": {
                    "type": "boolean"
                },
                "history": {
                    "type": "array",
                    "items": {}
                },
                "completed": {
                    "type": "boolean"
                },
                "collapseChecklist": {
                    "type": "boolean"
                },
                "checklist": {
                    "type": "array",
                    "items": {}
                },
                "createdAt": {
                    "type": "string"
                },
                "updatedAt": {
                    "type": "string"
                },
                "userId": {
                    "type": "string"
                },
                "isDue": {
                    "type": "boolean"
                },
                "id": {
                    "type": "string"
                }
            },
            "required": [
                "type",
                "text",
                "notes",
                "tags",
                "value",
                "priority",
                "attribute",
                "challenge",
                "group",
                "reminders",
                "byHabitica",
                "_id",
                "frequency",
                "everyX",
                "startDate",
                "repeat",
                "streak",
                "daysOfMonth",
                "weeksOfMonth",
                "nextDue",
                "yesterDaily",
                "history",
                "completed",
                "collapseChecklist",
                "checklist",
                "createdAt",
                "updatedAt",
                "userId",
                "isDue",
                "id"
            ]
        },
        "notifications": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "data": {
                            "type": "object",
                            "properties": {
                                "icon": {
                                    "type": "string"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "text": {
                                    "type": "string"
                                },
                                "destination": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "icon",
                                "title",
                                "text",
                                "destination"
                            ]
                        },
                        "seen": {
                            "type": "boolean"
                        },
                        "id": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "data",
                        "seen",
                        "id"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "data": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "title"
                            ]
                        },
                        "seen": {
                            "type": "boolean"
                        },
                        "id": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "data",
                        "seen",
                        "id"
                    ]
                }
            ]
        },
        "userV": {
            "type": "integer"
        },
        "appVersion": {
            "type": "string"
        }
    },
    "required": [
        "success",
        "data",
        "notifications",
        "userV",
        "appVersion"
    ]
}

post_move_task = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "data": {
            "type": "array",
            "items": [
                {
                    "type": "string"
                },
                {
                    "type": "string"
                },
                {
                    "type": "string"
                },
                {
                    "type": "string"
                },
                {
                    "type": "string"
                },
                {
                    "type": "string"
                }
            ]
        },
        "notifications": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "data": {
                            "type": "object",
                            "properties": {
                                "icon": {
                                    "type": "string"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "text": {
                                    "type": "string"
                                },
                                "destination": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "icon",
                                "title",
                                "text",
                                "destination"
                            ]
                        },
                        "seen": {
                            "type": "boolean"
                        },
                        "id": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "data",
                        "seen",
                        "id"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "data": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "title"
                            ]
                        },
                        "seen": {
                            "type": "boolean"
                        },
                        "id": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "data",
                        "seen",
                        "id"
                    ]
                }
            ]
        },
        "userV": {
            "type": "integer"
        },
        "appVersion": {
            "type": "string"
        }
    },
    "required": [
        "success",
        "data",
        "notifications",
        "userV",
        "appVersion"
    ]
}

delete_task = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "data": {
            "type": "object"
        },
        "notifications": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "data": {
                            "type": "object",
                            "properties": {
                                "icon": {
                                    "type": "string"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "text": {
                                    "type": "string"
                                },
                                "destination": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "icon",
                                "title",
                                "text",
                                "destination"
                            ]
                        },
                        "seen": {
                            "type": "boolean"
                        },
                        "id": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "data",
                        "seen",
                        "id"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "data": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "title"
                            ]
                        },
                        "seen": {
                            "type": "boolean"
                        },
                        "id": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "type",
                        "data",
                        "seen",
                        "id"
                    ]
                }
            ]
        },
        "userV": {
            "type": "integer"
        },
        "appVersion": {
            "type": "string"
        }
    },
    "required": [
        "success",
        "data",
        "notifications",
        "userV",
        "appVersion"
    ]
}
