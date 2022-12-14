import discord_typings


def message() -> discord_typings.MessageData:
    return {
        "type": 0,
        "tts": False,
        "timestamp": "2022-11-02T17:59:06.781000+00:00",
        "referenced_message": None,
        "pinned": False,
        "nonce": "1037425637981159424",
        "mentions": [],
        "mention_roles": [],
        "mention_everyone": False,
        "member": {
            "roles": ["1026431628223991828"],
            "premium_since": None,
            "pending": False,
            "nick": "reee",
            "mute": False,
            "joined_at": "2020-04-19T08:25:18.184000+00:00",
            "flags": 0,
            "deaf": False,
            "communication_disabled_until": None,
            "avatar": None,
        },
        "id": "1037425639030018179",
        "flags": 0,
        "embeds": [],
        "edited_timestamp": None,
        "content": "",
        "components": [],
        "channel_id": "1032200124732022835",
        "author": {
            "username": "LordOfPolls",
            "public_flags": 768,
            "id": "174918559539920897",
            "discriminator": "1010",
            "avatar_decoration": None,
            "avatar": "1f33250e68442f8b8f6e0cda5b4c7cb4",
        },
        "attachments": [],
        "guild_id": "701347683591389185",
    }


def nested_message() -> discord_typings.MessageData:
    return {
        "type": 0,
        "tts": False,
        "timestamp": "2022-11-02T17:58:06.781000+00:00",
        "edited_timestamp": "2022-11-02T17:59:06.781000+00:00",
        "referenced_message": None,
        "pinned": False,
        "nonce": "1037425637981159424",
        "mentions": [],
        "mention_roles": [],
        "mention_everyone": False,
        "member": {
            "roles": ["1026431628223991828"],
            "premium_since": None,
            "pending": False,
            "nick": "reee",
            "mute": False,
            "joined_at": "2020-04-19T08:25:18.184000+00:00",
            "flags": 0,
            "deaf": False,
            "communication_disabled_until": None,
            "avatar": None,
        },
        "id": "1037425639030018179",
        "flags": 0,
        "embeds": [
            {
                "title": "An embed title",
                "description": "This is a description",
                "color": 15548997,
                "fields": [
                    {"name": "Field 0", "value": "This is a field", "inline": False},
                    {"name": "Field 1", "value": "This is a field", "inline": False},
                    {"name": "Field 2", "value": "This is a field", "inline": False},
                    {"name": "Field 3", "value": "This is a field", "inline": False},
                    {"name": "Field 4", "value": "This is a field", "inline": False},
                    {"name": "Field 5", "value": "This is a field", "inline": False},
                    {"name": "Field 6", "value": "This is a field", "inline": False},
                    {"name": "Field 7", "value": "This is a field", "inline": False},
                    {"name": "Field 8", "value": "This is a field", "inline": False},
                    {"name": "Field 9", "value": "This is a field", "inline": False},
                    {"name": "Field 10", "value": "This is a field", "inline": False},
                    {"name": "Field 11", "value": "This is a field", "inline": False},
                    {"name": "Field 12", "value": "This is a field", "inline": False},
                    {"name": "Field 13", "value": "This is a field", "inline": False},
                    {"name": "Field 14", "value": "This is a field", "inline": False},
                    {"name": "Field 15", "value": "This is a field", "inline": False},
                    {"name": "Field 16", "value": "This is a field", "inline": False},
                    {"name": "Field 17", "value": "This is a field", "inline": False},
                    {"name": "Field 18", "value": "This is a field", "inline": False},
                    {"name": "Field 19", "value": "This is a field", "inline": False},
                    {"name": "Field 20", "value": "This is a field", "inline": False},
                    {"name": "Field 21", "value": "This is a field", "inline": False},
                    {"name": "Field 22", "value": "This is a field", "inline": False},
                    {"name": "Field 23", "value": "This is a field", "inline": False},
                    {"name": "Field 24", "value": "This is a field", "inline": False},
                ],
                "author": {
                    "name": "LordOfPolls",
                    "icon_url": "https://cdn.discordapp.com/avatars/174918559539920897/1f33250e68442f8b8f6e0cda5b4c7cb4.png",
                },
                "thumbnail": {
                    "url": "https://cdn.discordapp.com/avatars/174918559539920897/1f33250e68442f8b8f6e0cda5b4c7cb4.png"
                },
                "footer": {
                    "text": "This is a footer",
                    "icon_url": "https://cdn.discordapp.com/avatars/174918559539920897/1f33250e68442f8b8f6e0cda5b4c7cb4.png",
                },
            },
            {
                "title": "An embed title",
                "description": "This is a description",
                "color": 15548997,
                "fields": [
                    {"name": "Field 0", "value": "This is a field", "inline": False},
                    {"name": "Field 1", "value": "This is a field", "inline": False},
                    {"name": "Field 2", "value": "This is a field", "inline": False},
                    {"name": "Field 3", "value": "This is a field", "inline": False},
                    {"name": "Field 4", "value": "This is a field", "inline": False},
                    {"name": "Field 5", "value": "This is a field", "inline": False},
                    {"name": "Field 6", "value": "This is a field", "inline": False},
                    {"name": "Field 7", "value": "This is a field", "inline": False},
                    {"name": "Field 8", "value": "This is a field", "inline": False},
                    {"name": "Field 9", "value": "This is a field", "inline": False},
                    {"name": "Field 10", "value": "This is a field", "inline": False},
                    {"name": "Field 11", "value": "This is a field", "inline": False},
                    {"name": "Field 12", "value": "This is a field", "inline": False},
                    {"name": "Field 13", "value": "This is a field", "inline": False},
                    {"name": "Field 14", "value": "This is a field", "inline": False},
                    {"name": "Field 15", "value": "This is a field", "inline": False},
                    {"name": "Field 16", "value": "This is a field", "inline": False},
                    {"name": "Field 17", "value": "This is a field", "inline": False},
                    {"name": "Field 18", "value": "This is a field", "inline": False},
                    {"name": "Field 19", "value": "This is a field", "inline": False},
                    {"name": "Field 20", "value": "This is a field", "inline": False},
                    {"name": "Field 21", "value": "This is a field", "inline": False},
                    {"name": "Field 22", "value": "This is a field", "inline": False},
                    {"name": "Field 23", "value": "This is a field", "inline": False},
                    {"name": "Field 24", "value": "This is a field", "inline": False},
                ],
                "author": {
                    "name": "LordOfPolls",
                    "icon_url": "https://cdn.discordapp.com/avatars/174918559539920897/1f33250e68442f8b8f6e0cda5b4c7cb4.png",
                },
                "thumbnail": {
                    "url": "https://cdn.discordapp.com/avatars/174918559539920897/1f33250e68442f8b8f6e0cda5b4c7cb4.png"
                },
                "footer": {
                    "text": "This is a footer",
                    "icon_url": "https://cdn.discordapp.com/avatars/174918559539920897/1f33250e68442f8b8f6e0cda5b4c7cb4.png",
                },
            },
            {
                "title": "An embed title",
                "description": "This is a description",
                "color": 15548997,
                "fields": [
                    {"name": "Field 0", "value": "This is a field", "inline": False},
                    {"name": "Field 1", "value": "This is a field", "inline": False},
                    {"name": "Field 2", "value": "This is a field", "inline": False},
                    {"name": "Field 3", "value": "This is a field", "inline": False},
                    {"name": "Field 4", "value": "This is a field", "inline": False},
                    {"name": "Field 5", "value": "This is a field", "inline": False},
                    {"name": "Field 6", "value": "This is a field", "inline": False},
                    {"name": "Field 7", "value": "This is a field", "inline": False},
                    {"name": "Field 8", "value": "This is a field", "inline": False},
                    {"name": "Field 9", "value": "This is a field", "inline": False},
                    {"name": "Field 10", "value": "This is a field", "inline": False},
                    {"name": "Field 11", "value": "This is a field", "inline": False},
                    {"name": "Field 12", "value": "This is a field", "inline": False},
                    {"name": "Field 13", "value": "This is a field", "inline": False},
                    {"name": "Field 14", "value": "This is a field", "inline": False},
                    {"name": "Field 15", "value": "This is a field", "inline": False},
                    {"name": "Field 16", "value": "This is a field", "inline": False},
                    {"name": "Field 17", "value": "This is a field", "inline": False},
                    {"name": "Field 18", "value": "This is a field", "inline": False},
                    {"name": "Field 19", "value": "This is a field", "inline": False},
                    {"name": "Field 20", "value": "This is a field", "inline": False},
                    {"name": "Field 21", "value": "This is a field", "inline": False},
                    {"name": "Field 22", "value": "This is a field", "inline": False},
                    {"name": "Field 23", "value": "This is a field", "inline": False},
                    {"name": "Field 24", "value": "This is a field", "inline": False},
                ],
                "author": {
                    "name": "LordOfPolls",
                    "icon_url": "https://cdn.discordapp.com/avatars/174918559539920897/1f33250e68442f8b8f6e0cda5b4c7cb4.png",
                },
                "thumbnail": {
                    "url": "https://cdn.discordapp.com/avatars/174918559539920897/1f33250e68442f8b8f6e0cda5b4c7cb4.png"
                },
                "footer": {
                    "text": "This is a footer",
                    "icon_url": "https://cdn.discordapp.com/avatars/174918559539920897/1f33250e68442f8b8f6e0cda5b4c7cb4.png",
                },
            },
            {
                "title": "An embed title",
                "description": "This is a description",
                "color": 15548997,
                "fields": [
                    {"name": "Field 0", "value": "This is a field", "inline": False},
                    {"name": "Field 1", "value": "This is a field", "inline": False},
                    {"name": "Field 2", "value": "This is a field", "inline": False},
                    {"name": "Field 3", "value": "This is a field", "inline": False},
                    {"name": "Field 4", "value": "This is a field", "inline": False},
                    {"name": "Field 5", "value": "This is a field", "inline": False},
                    {"name": "Field 6", "value": "This is a field", "inline": False},
                    {"name": "Field 7", "value": "This is a field", "inline": False},
                    {"name": "Field 8", "value": "This is a field", "inline": False},
                    {"name": "Field 9", "value": "This is a field", "inline": False},
                    {"name": "Field 10", "value": "This is a field", "inline": False},
                    {"name": "Field 11", "value": "This is a field", "inline": False},
                    {"name": "Field 12", "value": "This is a field", "inline": False},
                    {"name": "Field 13", "value": "This is a field", "inline": False},
                    {"name": "Field 14", "value": "This is a field", "inline": False},
                    {"name": "Field 15", "value": "This is a field", "inline": False},
                    {"name": "Field 16", "value": "This is a field", "inline": False},
                    {"name": "Field 17", "value": "This is a field", "inline": False},
                    {"name": "Field 18", "value": "This is a field", "inline": False},
                    {"name": "Field 19", "value": "This is a field", "inline": False},
                    {"name": "Field 20", "value": "This is a field", "inline": False},
                    {"name": "Field 21", "value": "This is a field", "inline": False},
                    {"name": "Field 22", "value": "This is a field", "inline": False},
                    {"name": "Field 23", "value": "This is a field", "inline": False},
                    {"name": "Field 24", "value": "This is a field", "inline": False},
                ],
                "author": {
                    "name": "LordOfPolls",
                    "icon_url": "https://cdn.discordapp.com/avatars/174918559539920897/1f33250e68442f8b8f6e0cda5b4c7cb4.png",
                },
                "thumbnail": {
                    "url": "https://cdn.discordapp.com/avatars/174918559539920897/1f33250e68442f8b8f6e0cda5b4c7cb4.png"
                },
                "footer": {
                    "text": "This is a footer",
                    "icon_url": "https://cdn.discordapp.com/avatars/174918559539920897/1f33250e68442f8b8f6e0cda5b4c7cb4.png",
                },
            },
            {
                "title": "An embed title",
                "description": "This is a description",
                "color": 15548997,
                "fields": [
                    {"name": "Field 0", "value": "This is a field", "inline": False},
                    {"name": "Field 1", "value": "This is a field", "inline": False},
                    {"name": "Field 2", "value": "This is a field", "inline": False},
                    {"name": "Field 3", "value": "This is a field", "inline": False},
                    {"name": "Field 4", "value": "This is a field", "inline": False},
                    {"name": "Field 5", "value": "This is a field", "inline": False},
                    {"name": "Field 6", "value": "This is a field", "inline": False},
                    {"name": "Field 7", "value": "This is a field", "inline": False},
                    {"name": "Field 8", "value": "This is a field", "inline": False},
                    {"name": "Field 9", "value": "This is a field", "inline": False},
                    {"name": "Field 10", "value": "This is a field", "inline": False},
                    {"name": "Field 11", "value": "This is a field", "inline": False},
                    {"name": "Field 12", "value": "This is a field", "inline": False},
                    {"name": "Field 13", "value": "This is a field", "inline": False},
                    {"name": "Field 14", "value": "This is a field", "inline": False},
                    {"name": "Field 15", "value": "This is a field", "inline": False},
                    {"name": "Field 16", "value": "This is a field", "inline": False},
                    {"name": "Field 17", "value": "This is a field", "inline": False},
                    {"name": "Field 18", "value": "This is a field", "inline": False},
                    {"name": "Field 19", "value": "This is a field", "inline": False},
                    {"name": "Field 20", "value": "This is a field", "inline": False},
                    {"name": "Field 21", "value": "This is a field", "inline": False},
                    {"name": "Field 22", "value": "This is a field", "inline": False},
                    {"name": "Field 23", "value": "This is a field", "inline": False},
                    {"name": "Field 24", "value": "This is a field", "inline": False},
                ],
                "author": {
                    "name": "LordOfPolls",
                    "icon_url": "https://cdn.discordapp.com/avatars/174918559539920897/1f33250e68442f8b8f6e0cda5b4c7cb4.png",
                },
                "thumbnail": {
                    "url": "https://cdn.discordapp.com/avatars/174918559539920897/1f33250e68442f8b8f6e0cda5b4c7cb4.png"
                },
                "footer": {
                    "text": "This is a footer",
                    "icon_url": "https://cdn.discordapp.com/avatars/174918559539920897/1f33250e68442f8b8f6e0cda5b4c7cb4.png",
                },
            },
        ],
        "content": "Test",
        "components": [
            {
                "components": [
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                ],
                "type": 1,
            },
            {
                "components": [
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                ],
                "type": 1,
            },
            {
                "components": [
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                ],
                "type": 1,
            },
            {
                "components": [
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                ],
                "type": 1,
            },
            {
                "components": [
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                    {
                        "style": 1,
                        "label": "Click me!",
                        "custom_id": "click",
                        "disabled": False,
                        "type": 2,
                    },
                ],
                "type": 1,
            },
        ],
        "channel_id": "1032200124732022835",
        "author": {
            "username": "LordOfPolls",
            "public_flags": 768,
            "id": "174918559539920897",
            "discriminator": "1010",
            "avatar_decoration": None,
            "avatar": "1f33250e68442f8b8f6e0cda5b4c7cb4",
        },
        "attachments": [],
        "guild_id": "701347683591389185",
    }


def guild() -> discord_typings.GuildData:
    return {
        "premium_progress_bar_enabled": False,
        "emojis": [
            {
                "roles": ["743376965053972601"],
                "require_colons": True,
                "name": "indicator",
                "managed": False,
                "id": "872419861190574090",
                "available": True,
                "animated": False,
            },
            {
                "roles": [],
                "require_colons": True,
                "name": "whatDidYouJustPost",
                "managed": False,
                "id": "929464862625652817",
                "available": True,
                "animated": False,
            },
            {
                "roles": [],
                "require_colons": True,
                "name": "last",
                "managed": False,
                "id": "945479422335680514",
                "available": True,
                "animated": False,
            },
            {
                "roles": [],
                "require_colons": True,
                "name": "forward",
                "managed": False,
                "id": "945479422423748639",
                "available": True,
                "animated": False,
            },
            {
                "roles": [],
                "require_colons": True,
                "name": "first",
                "managed": False,
                "id": "945479422700576768",
                "available": True,
                "animated": False,
            },
            {
                "roles": [],
                "require_colons": True,
                "name": "back",
                "managed": False,
                "id": "945479422704775188",
                "available": True,
                "animated": False,
            },
            {
                "roles": [],
                "require_colons": True,
                "name": "callback",
                "managed": False,
                "id": "945479422725726208",
                "available": True,
                "animated": False,
            },
            {
                "roles": [],
                "require_colons": True,
                "name": "loading",
                "managed": False,
                "id": "950666903540625418",
                "available": True,
                "animated": True,
            },
        ],
        "owner_id": "174918559539920897",
        "presences": [],
        "premium_tier": 0,
        "splash": None,
        "guild_scheduled_events": [],
        "features": [
            "NEW_THREAD_PERMISSIONS",
            "MEMBER_VERIFICATION_GATE_ENABLED",
            "THREADS_ENABLED",
            "BOT_DEVELOPER_EARLY_ACCESS",
            "PREVIEW_ENABLED",
            "COMMUNITY",
            "TEXT_IN_VOICE_ENABLED",
            "NEWS",
            "AUTO_MODERATION",
            "WELCOME_SCREEN_ENABLED",
        ],
        "channels": [
            {
                "version": 0,
                "type": 0,
                "topic": None,
                "rate_limit_per_user": 0,
                "position": 0,
                "permission_overwrites": [
                    {
                        "type": 0,
                        "id": "701347683591389185",
                        "deny": "3072",
                        "allow": "0",
                    }
                ],
                "parent_id": None,
                "nsfw": False,
                "name": "Rules",
                "last_message_id": "1023862307329151097",
                "id": "820046256398925855",
                "flags": 0,
            },
            {
                "version": 0,
                "type": 4,
                "position": 0,
                "permission_overwrites": [],
                "parent_id": None,
                "name": "Data Mining",
                "id": "1026431953085407232",
                "flags": 0,
            },
            {
                "version": 0,
                "type": 0,
                "topic": None,
                "rate_limit_per_user": 0,
                "position": 1,
                "permission_overwrites": [
                    {
                        "type": 0,
                        "id": "701347683591389185",
                        "deny": "0",
                        "allow": "18432",
                    },
                    {
                        "type": 0,
                        "id": "1026448436461060108",
                        "deny": "0",
                        "allow": "537316368",
                    },
                ],
                "parent_id": "1026431953085407232",
                "nsfw": False,
                "name": "build-changes",
                "last_message_id": "1037386619415695390",
                "id": "1026432004134277120",
                "flags": 0,
            },
            {
                "version": 0,
                "type": 0,
                "topic": None,
                "rate_limit_per_user": 0,
                "position": 2,
                "permission_overwrites": [],
                "parent_id": "1026431953085407232",
                "nsfw": False,
                "name": "data-mining-tweets",
                "last_message_id": "1026432286801010738",
                "id": "1026432253758279701",
                "flags": 0,
            },
            {
                "version": 0,
                "type": 4,
                "position": 2,
                "permission_overwrites": [],
                "parent_id": None,
                "name": "testing",
                "id": "1026435541903884369",
                "flags": 0,
            },
            {
                "version": 0,
                "type": 0,
                "topic": None,
                "rate_limit_per_user": 0,
                "position": 4,
                "permission_overwrites": [],
                "parent_id": "1026435541903884369",
                "nsfw": False,
                "name": "commands",
                "last_message_id": "1034529384616443997",
                "id": "1026437499402322020",
                "flags": 0,
            },
            {
                "version": 0,
                "type": 4,
                "position": 1,
                "permission_overwrites": [],
                "parent_id": None,
                "name": "non-testing",
                "id": "1026442309799252018",
                "flags": 0,
            },
            {
                "version": 0,
                "type": 0,
                "topic": None,
                "rate_limit_per_user": 0,
                "position": 5,
                "permission_overwrites": [],
                "parent_id": "1026442309799252018",
                "nsfw": False,
                "name": "general",
                "last_message_id": "1029786598075813919",
                "id": "1026442352669237298",
                "flags": 0,
            },
            {
                "version": 0,
                "type": 0,
                "topic": None,
                "rate_limit_per_user": 0,
                "position": 6,
                "permission_overwrites": [],
                "parent_id": "1026431953085407232",
                "nsfw": False,
                "name": "resources",
                "last_message_id": "1026448172916146236",
                "id": "1026447690193711164",
                "flags": 0,
            },
            {
                "version": 1666175910067,
                "user_limit": 0,
                "type": 2,
                "rtc_region": None,
                "rate_limit_per_user": 0,
                "position": 0,
                "permission_overwrites": [],
                "parent_id": "1026435541903884369",
                "nsfw": False,
                "name": "lofi-radio",
                "last_message_id": "1032194698854547486",
                "id": "1032194696891609128",
                "flags": 0,
                "bitrate": 64000,
            },
            {
                "version": 1666166087161,
                "type": 0,
                "topic": None,
                "rate_limit_per_user": 0,
                "position": 7,
                "permission_overwrites": [],
                "parent_id": "1026435541903884369",
                "nsfw": False,
                "name": "test-174918559539920897",
                "last_message_id": "1037425639030018179",
                "id": "1032200124732022835",
                "flags": 0,
            },
        ],
        "stickers": [],
        "large": False,
        "lazy": True,
        "premium_subscription_count": 0,
        "hub_type": None,
        "icon": "cac5a2fac758e0fec3de9222a358e315",
        "region": "deprecated",
        "guild_hashes": {
            "version": 1,
            "roles": {"omitted": False, "hash": "nVpegA"},
            "metadata": {"omitted": False, "hash": "pWw/gw"},
            "channels": {"omitted": False, "hash": "PRHkjA"},
        },
        "id": "701347683591389185",
        "banner": None,
        "verification_level": 1,
        "nsfw": False,
        "system_channel_flags": 0,
        "preferred_locale": "en-US",
        "vanity_url_code": None,
        "joined_at": "2022-06-17T05:48:52.645000+00:00",
        "nsfw_level": 0,
        "max_stage_video_channel_users": 0,
        "threads": [],
        "discovery_splash": None,
        "max_members": 500000,
        "public_updates_channel_id": "820046256398925855",
        "description": None,
        "application_id": None,
        "application_command_counts": {"3": 3, "1": 31},
        "embedded_activities": [],
        "voice_states": [],
        "default_message_notifications": 1,
        "stage_instances": [],
        "afk_timeout": 300,
        "roles": [
            {
                "version": 0,
                "unicode_emoji": None,
                "tags": {},
                "position": 0,
                "permissions": "0",
                "name": "@everyone",
                "mentionable": False,
                "managed": False,
                "id": "701347683591389185",
                "icon": None,
                "hoist": False,
                "flags": 0,
                "color": 0,
            },
            {
                "version": 0,
                "unicode_emoji": None,
                "tags": {},
                "position": 3,
                "permissions": "1071594602496",
                "name": "bot in use",
                "mentionable": False,
                "managed": False,
                "id": "927975517456588873",
                "icon": None,
                "hoist": True,
                "flags": 0,
                "color": 3447003,
            },
            {
                "version": 0,
                "unicode_emoji": None,
                "tags": {"bot_id": "701347878311821373"},
                "position": 2,
                "permissions": "8",
                "name": "TestyBoi",
                "mentionable": False,
                "managed": True,
                "id": "987232343473397774",
                "icon": None,
                "hoist": False,
                "flags": 0,
                "color": 0,
            },
            {
                "version": 0,
                "unicode_emoji": None,
                "tags": {},
                "position": 1,
                "permissions": "8",
                "name": "Access Granted",
                "mentionable": False,
                "managed": False,
                "id": "1026431628223991828",
                "icon": None,
                "hoist": False,
                "flags": 0,
                "color": 2067276,
            },
            {
                "version": 0,
                "unicode_emoji": None,
                "tags": {"bot_id": "379343322545782784"},
                "position": 4,
                "permissions": "8",
                "name": "Rebecca",
                "mentionable": False,
                "managed": True,
                "id": "1026434808760500308",
                "icon": None,
                "hoist": False,
                "flags": 0,
                "color": 0,
            },
            {
                "version": 0,
                "unicode_emoji": None,
                "tags": {"bot_id": "507415798189654016"},
                "position": 1,
                "permissions": "537315344",
                "name": "Datamine Updates",
                "mentionable": False,
                "managed": True,
                "id": "1026448436461060108",
                "icon": None,
                "hoist": False,
                "flags": 0,
                "color": 0,
            },
            {
                "version": 0,
                "unicode_emoji": None,
                "tags": {"bot_id": "903968203779215401"},
                "position": 1,
                "permissions": "377957468160",
                "name": "Inquiry",
                "mentionable": False,
                "managed": True,
                "id": "1026449199543357453",
                "icon": None,
                "hoist": False,
                "flags": 0,
                "color": 0,
            },
        ],
        "explicit_content_filter": 2,
        "unavailable": False,
        "system_channel_id": None,
        "rules_channel_id": "820046256398925855",
        "name": "NAFF Developer Playground",
        "mfa_level": 0,
        "members": [
            {
                "user": {
                    "username": "Testy Boi",
                    "public_flags": 0,
                    "id": "701347878311821373",
                    "discriminator": "3355",
                    "bot": True,
                    "avatar": "2d3b4ed587797e683167a355c360d9dc",
                },
                "roles": ["927975517456588873", "987232343473397774"],
                "premium_since": None,
                "pending": False,
                "nick": None,
                "mute": False,
                "joined_at": "2022-06-17T05:48:52.645000+00:00",
                "flags": 0,
                "deaf": False,
                "communication_disabled_until": None,
                "avatar": None,
            }
        ],
        "afk_channel_id": None,
        "member_count": 11,
        "max_video_channel_users": 25,
    }
