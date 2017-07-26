=====
Usage
=====

TODO: say that content.padding isn't always took into consideration

This article is a tutorial for ``nider`` package and at the same time it is a full reference of all ``nider`` models and possibilities.

***********
Image units
***********

There are three main units each ``nider.Image`` can consist of:

- header
- paragraph
- linkback

.. image:: images/available_units.png

Paragraph unit is required for each image whereas header and linkback are optional.

Each of the units is represented by a class in ``nider.models``:

- ``nider.models.Header``
- ``nider.models.Paragraph``
- ``nider.models.Linkback``

``nider.models.Header``
=========================

.. class:: Header(text, \
                 fontfullpath, fontsize=18, \
                 text_width=21, line_padding=6, \
                 color='#000', drop_shadow=False, shadowcolor='#646464', \
                 align='center')

    Base class for the header unit

    :param str text: Text used in the header
    :param str fontfullpath: Path to the font used in the header
    :param int text_width: Header's text width - number of characters in a line
    :param int line_padding: Header's line padding - padding (in pixels) between the lines
    :param int fontsize: Size of the font
    :param color: Either hex or rgb representation of text color
    :type color: str or tuple(int, int, int)
    :param bool drop_shadow: Boolean flag that indicates if text has to drop shadow
    :param shadowcolor: Either hex or rgb representation of shadowcolor color
    :type shadowcolor: str or tuple(int, int, int)
    :param align: Side with respect to which the text will be aligned
    :type align: 'left' or 'center' or 'right'
    :raises nider.exceptions.InvalidAlignException: if ``align`` is not one of 'left' or 'center' or 'right'
    :raises nider.exceptions.DefaultFontWarning: if ``fontfullpath`` is ``None``
    :raises nider.exceptions.FontNotFoundWarning: if ``fontfullpath`` does not exist

Example
-------

.. code-block:: python

    from nider.models import Header

    header = Header(text='Your super interesting title!',
                    fontfullpath='/home/me/.local/share/fonts/Roboto/Roboto-Bold.ttf',
                    fontsize=30,
                    text_width=40,
                    align='left',
                    color='#ededed'
                    )


``nider.models.Paragraph``
============================

The class has the same attribures and behaviour as ``nider.models.Header``.

.. class:: Paragraph(text, \
                 fontfullpath, fontsize=18, \
                 text_width=21, line_padding=6, \
                 color='#000', drop_shadow=False, shadowcolor='#646464', \
                 align='center')

    Base class for the paragraph unit

    :param str text: Text used in the paragraph
    :param str fontfullpath: Path to the font used in the paragraph
    :param int text_width: Paragraph's text width - number of characters in a line
    :param int line_padding: Paragraph's line padding - padding (in pixels) between the lines
    :param int fontsize: Size of the font
    :param color: Either hex or rgb representation of text color
    :type color: str or tuple(int, int, int)
    :param bool drop_shadow: Boolean flag that indicates if text has to drop shadow
    :param shadowcolor: Either hex or rgb representation of shadowcolor color
    :type shadowcolor: str or tuple(int, int, int)
    :param align: Side with respect to which the text will be aligned
    :type align: 'left' or 'center' or 'right'
    :raises nider.exceptions.InvalidAlignException: if ``align`` is not one of 'left' or 'center' or 'right'
    :raises nider.exceptions.DefaultFontWarning: if ``fontfullpath`` is ``None``
    :raises nider.exceptions.FontNotFoundWarning: if ``fontfullpath`` does not exist

Example
-------

.. code-block:: python

    from nider.models import Paragraph

    para = Paragraph(text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                    fontfullpath='/home/me/.local/share/fonts/Roboto/Roboto-Medium.ttf',
                     fontsize=29,
                     text_width=65,
                     align='left',
                     color='#ededed'
                     )


``nider.models.Linkback``
===========================

.. class:: Linkback(text, \
                 fontfullpath, fontsize=18, \
                 color='#000', drop_shadow=False, shadowcolor='#646464', \
                 align='center', bottom_padding=20)

    Base class for the linkback unit

    :param str text: Text used in the linkback
    :param str fontfullpath: Path to the font used in the linkback
    :param int fontsize: Size of the font
    :param color: Either hex or rgb representation of text color
    :type color: str or tuple(int, int, int)
    :param bool drop_shadow: Boolean flag that indicates if text has to drop shadow
    :param shadowcolor: Either hex or rgb representation of shadowcolor color
    :type shadowcolor: str or tuple(int, int, int)
    :param align: Side with respect to which the text will be aligned
    :type align: 'left' or 'center' or 'right'
    :param int bottom_padding: Linkback's bottom padding - padding (in pixels) between the bottom of the image and the linkback itself
    :raises nider.exceptions.InvalidAlignException: if ``align`` is not one of 'left' or 'center' or 'right'
    :raises nider.exceptions.DefaultFontWarning: if ``fontfullpath`` is ``None``
    :raises nider.exceptions.FontNotFoundWarning: if ``fontfullpath`` does not exist

Example
-------

.. code-block:: python

    from nider.models import Linkback

    linkback = Linkback(text='foo.com | @username',
                        fontfullpath='/home/me/.local/share/fonts/Roboto/Roboto-Bold.ttf',
                        fontsize=24,
                        color='#ededed'
                        )

*************
Image content
*************

In order to aggregate all of the units together you need to create an instance of ``nider.models.Content`` class.

``nider.models.Content``
==========================

.. class:: Content(paragraph, header=None, linkback=None, padding=45)

    Class that aggregates different units into a sigle object

    :param nider.models.Paragraph paragraph: Paragraph that will be used
    :param nider.models.Header header: Header that will be used
    :param nider.models.Linkback linkback: Linkback that will be used
    :param int padding: Content's padding - padding (in pixels) between the units

Example
-------

.. code-block:: python

    from nider.models import Content
    from nider.models import Linkback
    from nider.models import Paragraph

    para = Paragraph(...)

    linkback = Linkback(...)

    content = Content(para, linkback=linkback, padding=60)


*********************
Initializing an image
*********************

After the content is prepared it's the right time to initialize an image. In ``nider`` a basic image is represented by ``nider.models.Image``

``nider.models.Image``
========================

.. class:: Image(content, fullpath, width=1080, height=1080)

    Base class for a text based image

    :param nider.models.Content content: Content object that has units to be rendered
    :param str fullpath: Path where the image has to be saved
    :param int width: Width of the image
    :param int height: Height of the image
    :raises AttributeError: if it's impossible to create a file at ``fullpath`` path
    :raises AttributeError: if width <= 0 or height <= 0

Example
-------

.. code-block:: python

    from nider.models import Content
    from nider.models import Image

    content = Content(...)

    img = Image(content,
                fullpath='example.png',
                width=500,
                height=500
                )

Social media images
-------------------

``nider`` comes with some pre-built models that can be used to generate images for some social networks. These are subclasses of ``nider.models.Image`` with changed size

Instagram
^^^^^^^^^

 - ``nider.models.InstagramSquarePost`` - 1080x1080 image
 - ``nider.models.InstagramPortraitPost`` - 1080x1350 image
 - ``nider.models.InstagramLandscapePost`` - 1080x566 image

Facebook
^^^^^^^^

 - ``nider.models.FacebookSquarePost`` - 470x470 image
 - ``nider.models.FacebookLandscapePost`` - 1024x512 image

Twitter
^^^^^^^

 - ``nider.models.TwitterPost`` - 1024x512 image
 - ``nider.TwitterLargeCard`` - 506x506 image

============

I highly recommend reading this `post <https://blog.bufferapp.com/ideal-image-sizes-social-media-posts>`_ if you are curious about what are the right image sizes for social media images.

********************
Drawing on the image
********************

Having an instance of ``nider.models.Image`` we are ready to create a real image.

``nider`` comes with 3 options of drawing your image:

 - ``Image.draw_on_texture`` - draws preinitialized image and its attributes on a texture. **nider takes care of filling image of any size with textrure you privide. You don't need to create textured images by pasting texture mulpitle times in Photoshop or Gimp.**

 - ``Image.draw_on_bg`` - Draws preinitialized image and its attributes on a colored background. nider uses a color you provide to fill the image and then draws the content.

 - ``Image.draw_on_image`` - Draws preinitialized image and its attributes on an image. Content will be drawn directly on the image you provide.


``Image.draw_on_texture``
=========================

.. method:: draw_on_texture(texture_path=None)

    Draws preinitiated image and its attributes on a texture. If ``texture_path``
    is set to ``None``, takes random textures from ``textures/``

    :param str texture_path: Path of the texture to use

    :raises FileNotFoundError: if the file at ``texture_path`` cannot be found
    :raises nider.exceptions.ImageSizeFixedWarning: if the image size has to be adjusted to the provided content's size because the content takes much space


Example
-------

.. code-block:: python

    from nider.models import Content
    from nider.models import Image

    content = Content(...)

    img = Image(content,
                fullpath='example.png',
                width=500,
                height=500
                )

    img.draw_on_texture('example_texture.png')


Check the full example `here <https://github.com/pythad/nider/blob/master/examples/draw_on_texture_example/script.py>`_ 

============

``nider`` comes with a `huge bundle of textures <https://github.com/pythad/nider/tree/master/nider/textures>`_. As for now you need to copy them to your machine if you want to use any of them.

``Image.draw_on_bg``
=========================

.. method:: draw_on_bg(bgcolor=None)

    Draws preinitiated image and its attributes on a colored background. If ``bgcolor``
    is set to ``None``, random ``nider.colors.colormap.FLAT_UI`` color is generated

    :param bgcolor: Either hex or rgb representation of background color
    :type bgcolor: str or tuple(int, int, int)

    :raises nider.exceptions.ImageSizeFixedWarning: if the image size has to be adjusted to the provided content's size because the content takes much space



Example
-------

.. code-block:: python

    from nider.models import Content
    from nider.models import Image

    content = Content(...)

    img = Image(content,
                fullpath='example.png',
                width=500,
                height=500
                )

    img.draw_on_bg('#efefef')

Check the full example `here <https://github.com/pythad/nider/blob/master/examples/draw_on_bg_example/script.py>`_ 

``Image.draw_on_image``
=========================

.. method:: draw_on_image(image_path)

    Draws preinitiated image and its attributes on an image. Image size will be changed to the size of provided image.

    :param str image_path: Path of the image to draw on

    :raises FileNotFoundError: if the file at ``image_path`` cannot be found

Example
-------

.. code-block:: python

    from nider.models import Content
    from nider.models import Image

    content = Content(...)

    img = Image(content,
                fullpath='example.png',
                width=500,
                height=500
                )

    img.draw_on_image('example_bg.jpg')

Check the full example `here <https://github.com/pythad/nider/blob/master/examples/draw_on_image_example/script.py>`_ 

============

That's it. After any of draw methods has been called and successfully completed the new image will be saved to ``Image.fullpath``.