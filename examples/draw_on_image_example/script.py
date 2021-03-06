from nider.models import Content
from nider.models import Header
from nider.models import Linkback
from nider.models import Paragraph
from nider.models import Image

# TODO: change this fontpath to the fontpath on your machine
roboto = '/home/ovd/.local/share/fonts/Roboto/'

header = Header(text='Your super interesting title!',
                fontfullpath=roboto + 'Roboto-Bold.ttf',
                fontsize=30,
                text_width=40,
                align='left',
                color='#ededed',
                drop_shadow=True,
                shadowcolor='#999'
                )

para = Paragraph(text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 fontfullpath=roboto + 'Roboto-Medium.ttf',
                 fontsize=29,
                 text_width=65,
                 align='left',
                 color='#ededed',
                 drop_shadow=True,
                 shadowcolor='#999'
                 )

linkback = Linkback(text='foo.com | @username',
                    fontfullpath=roboto + 'Roboto-Bold.ttf',
                    fontsize=24,
                    color='#ededed',
                    drop_shadow=True,
                    shadowcolor='#999'
                    )

content = Content(para, header=header, linkback=linkback, padding=60)

img = Image(content,
            fullpath='result.png',
            width=1080,
            height=720
            )

# TODO: change this image path to the image path on your machine
img.draw_on_image('bg.jpg')
