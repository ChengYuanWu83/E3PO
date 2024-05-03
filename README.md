# Introduction
This project originates from the [E3PO project](https://github.com/bytedance/E3PO)

# Problems in ERP Method
In ERP method, 360 video is projected by equirectangular projection. In equirectangular projection, although the uniformity of the steps used to sample the polar and azimuth angles, the obtained distribution of the pixels on the sphere is not at all uniform. As can be seen in Fig. 2.8, two regions of equal area in the panorama (the blue at the equator and the red at the poles) correspond to two regions of strongly different sizes on the sphere. This naturally causes huge visual distortion and can limit the performance of image processing algorithms. For the two neighboring points on the sphere can be mapped at extreme positions on the panorama.

＃ Proposed Solution
To avoid the spherical distortion, we change the projection method to the cubemap projection. In cubemap projection, it projects the spherical image onto the six faces of a cube centered around the sphere center. The cube is then unfolded, and can even be re-arranged to form an image with a 2D shape. It is worth noting that the projection on each individual face mimics a perspective camera capture with a field of view of π/2 × π/2.
