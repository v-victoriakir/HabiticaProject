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
