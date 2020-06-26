'''
In general, your lighting conditions should have three primary goals. Let’s review them below.

1) High Contrast
Maximize the contrast between the Regions of Interest in your image (objects
    you want to detect, extract, describe classify, manipulate, etc. should have
    sufficiently high contrast from the rest of the image so they are easily 
    detectable).

2) Generalizable
Your lighting conditions should be consistent enough that they work well from one
    object to the next. If our goal is to identify various United States coins 
    in an image, our lighting conditions should be generalizable enough to 
    facilitate in the coin identification, whether we are examining a penny,
    nickel, dime, or quarter.

3) Stable
Having stable, consistent, and repeatable lighting conditions is the holy grail 
of computer vision application development. However, it’s often hard (if not 
impossible) to guarantee — this is especially true if we are developing computer
vision algorithms that are intended to work in outdoor lighting conditions.
As the time of day changes, clouds roll in over the sun, and rain starts to pour,
our lighting conditions will obviously change.

'''


'''
COLOR SPACES
1) RGB
2) HSV
    Hue: Which “pure” color we are examining. For example, all shadows and tones
        of the color “red” will have the same Hue.
    Saturation: How “white” the color is. A fully saturated color would be pure,
        as in “pure red.” And a color with zero saturation would be pure white.
    Value: The Value allows us to control the lightness of our color. A Value of
        zero would indicate pure black, whereas increasing the value would produce 
        lighter colors.
'''


'''
NO CODE

'''
