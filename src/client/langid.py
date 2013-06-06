#!/usr/bin/python

# Definitions for USB language identifiers (Version 1.0)
# see http://www.usb.org/developers/docs/USB_LANGIDs.pdf

LANGID = {
        'Afrikaans'                    : 0x0436,
        'Albanian'                     : 0x041c,
        'Arabic (Saudi Arabia)'        : 0x0401,
        'Arabic (Iraq)'                : 0x0801,
        'Arabic (Egypt)'               : 0x0c01,
        'Arabic (Libya)'               : 0x1001,
        'Arabic (Algeria)'             : 0x1401,
        'Arabic (Morocco)'             : 0x1801,
        'Arabic (Tunisia)'             : 0x1c01,
        'Arabic (Oman)'                : 0x2001,
        'Arabic (Yemen)'               : 0x2401,
        'Arabic (Syria)'               : 0x2801,
        'Arabic (Jordan)'              : 0x2c01,
        'Arabic (Lebanon)'             : 0x3001,
        'Arabic (Kuwait)'              : 0x3401,
        'Arabic (U.A.E.)'              : 0x3801,
        'Arabic (Bahrain)'             : 0x3c01,
        'Arabic (Qatar)'               : 0x4001,
        'Armenian'                     : 0x042b,
        'Assamese'                     : 0x044d,
        'Azeri (Latin)'                : 0x042c,
        'Azeri (Cyrillic)'             : 0x082c,
        'Basque'                       : 0x042d,
        'Belarussian'                  : 0x0423,
        'Bengali'                      : 0x0445,
        'Bulgarian'                    : 0x0402,
        'Burmese'                      : 0x0455,
        'Catalan'                      : 0x0403,
        'Chinese (Taiwan)'             : 0x0404,
        'Chinese (PRC)'                : 0x0804,
        'Chinese (Hong Kong SAR, PRC)' : 0x0c04,
        'Chinese (Singapore)'          : 0x1004,
        'Chinese (Macau SAR)'          : 0x1404,
        'Croatian'                     : 0x041a,
        'Czech'                        : 0x0405,
        'Danish'                       : 0x0406,
        'Dutch (Netherlands)'          : 0x0413,
        'Dutch (Belgium)'              : 0x0813,
        'English (United States)'      : 0x0409,
        'English (United Kingdom)'     : 0x0809,
        'English (Australian)'         : 0x0c09,
        'English (Canadian)'           : 0x1009,
        'English (New Zealand)'        : 0x1409,
        'English (Ireland)'            : 0x1809,
        'English (South Africa)'       : 0x1c09,
        'English (Jamaica)'            : 0x2009,
        'English (Caribbean)'          : 0x2409,
        'English (Belize)'             : 0x2809,
        'English (Trinidad)'           : 0x2c09,
        'English (Zimbabwe)'           : 0x3009,
        'English (Philippines)'        : 0x3409,
        'Estonian'                     : 0x0425,
        'Faeroese'                     : 0x0438,
        'Farsi'                        : 0x0429,
        'Finnish'                      : 0x040b,
        'French (Standard)'            : 0x040c,
        'French (Belgian)'             : 0x080c,
        'French (Canadian)'            : 0x0c0c,
        'French (Switzerland)'         : 0x100c,
        'French (Luxembourg)'          : 0x140c,
        'French (Monaco)'              : 0x180c,
        'Georgian'                     : 0x0437,
        'German (Standard)'            : 0x0407,
        'German (Switzerland)'         : 0x0807,
        'German (Austria)'             : 0x0c07,
        'German (Luxembourg)'          : 0x1007,
        'German (Liechtenstein)'       : 0x1407,
        'Greek'                        : 0x0408,
        'Gujarati'                     : 0x0447,
        'Hebrew'                       : 0x040d,
        'Hindi'                        : 0x0439,
        'Hungarian'                    : 0x040e,
        'Icelandic'                    : 0x040f,
        'Indonesian'                   : 0x0421,
        'Italian (Standard)'           : 0x0410,
        'Italian (Switzerland)'        : 0x0810,
        'Japanese'                     : 0x0411,
        'Kannada'                      : 0x044b,
        'Kashmiri (India)'             : 0x0860,
        'Kazakh'                       : 0x043f,
        'Konkani'                      : 0x0457,
        'Korean'                       : 0x0412,
        'Korean (Johab)'               : 0x0812,
        'Latvian'                      : 0x0426,
        'Lithuanian'                   : 0x0427,
        'Lithuanian (Classic)'         : 0x0827,
        'Macedonian'                   : 0x042f,
        'Malay (Malaysian)'            : 0x043e,
        'Malay (Brunei Darussalam)'    : 0x083e,
        'Malayalam'                    : 0x044c,
        'Manipuri'                     : 0x0458,
        'Marathi'                      : 0x044e,
        'Nepali (India)'               : 0x0861,
        'Norwegian (Bokmal)'           : 0x0414,
        'Norwegian (Nynorsk)'          : 0x0814,
        'Oriya'                        : 0x0448,
        'Polish'                       : 0x0415,
        'Portuguese (Brazil)'          : 0x0416,
        'Portuguese (Standard)'        : 0x0816,
        'Punjabi'                      : 0x0446,
        'Romanian'                     : 0x0418,
        'Russian'                      : 0x0419,
        'Sanskrit'                     : 0x044f,
        'Serbian (Cyrillic)'           : 0x0c1a,
        'Serbian (Latin)'              : 0x081a,
        'Sindhi'                       : 0x0459,
        'Slovak'                       : 0x041b,
        'Slovenian'                    : 0x0424,
        'Spanish (Traditional Sort)'   : 0x040a,
        'Spanish (Mexican)'            : 0x080a,
        'Spanish (Modern Sort)'        : 0x0c0a,
        'Spanish (Guatemala)'          : 0x100a,
        'Spanish (Costa Rica)'         : 0x140a,
        'Spanish (Panama)'             : 0x180a,
        'Spanish (Dominican Republic)' : 0x1c0a,
        'Spanish (Venezuela)'          : 0x200a,
        'Spanish (Colombia)'           : 0x240a,
        'Spanish (Peru)'               : 0x280a,
        'Spanish (Argentina)'          : 0x2c0a,
        'Spanish (Ecuador)'            : 0x300a,
        'Spanish (Chile)'              : 0x340a,
        'Spanish (Uruguay)'            : 0x380a,
        'Spanish (Paraguay)'           : 0x3c0a,
        'Spanish (Bolivia)'            : 0x400a,
        'Spanish (El Salvador)'        : 0x440a,
        'Spanish (Honduras)'           : 0x480a,
        'Spanish (Nicaragua)'          : 0x4c0a,
        'Spanish (Puerto Rico)'        : 0x500a,
        'Sutu'                         : 0x0430,
        'Swahili (Kenya)'              : 0x0441,
        'Swedish'                      : 0x041d,
        'Swedish (Finland)'            : 0x081d,
        'Tamil'                        : 0x0449,
        'Tatar (Tatarstan)'            : 0x0444,
        'Telugu'                       : 0x044a,
        'Thai'                         : 0x041e,
        'Turkish'                      : 0x041f,
        'Ukrainian'                    : 0x0422,
        'Urdu (Pakistan)'              : 0x0420,
        'Urdu (India)'                 : 0x0820,
        'Uzbek (Latin)'                : 0x0443,
        'Uzbek (Cyrillic)'             : 0x0843,
        'Vietnamese'                   : 0x042a,
        'HID (Usage Data Descriptor)'  : 0x04ff,
        'HID (Vendor Defined 1)'       : 0xf0ff,
        'HID (Vendor Defined 2)'       : 0xf4ff,
        'HID (Vendor Defined 3)'       : 0xf8ff,
        'HID (Vendor Defined 4)'       : 0xfcff,
        }
