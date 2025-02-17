import numpy as np
import cv2

def draw(img, corners, imgpts):
    corner = tuple(np.round(corners[0].ravel()).astype(int))
    print(corner)
    img = cv2.line(img, corner, tuple(np.round((imgpts[0].ravel()).astype(int))), (255, 0, 0), 5)
    img = cv2.line(img, corner, tuple(np.round((imgpts[1].ravel()).astype(int))), (0, 255, 0), 5)
    img = cv2.line(img, corner, tuple(np.round((imgpts[2].ravel().astype(int)))), (0, 0, 255), 5)
    return img

def camera_pose_from_homography(Kinv, H):
    '''Calculate camera pose from Homography.

    Args:
       Kinv: inverse intrinsic camera matrix
       H: homography matrix
    Returns:
       R: rotation matrix
       T: translation vector
    '''
    H = np.transpose(H)
    # the scale factor
    l = 1 / np.linalg.norm(np.dot(Kinv, H[0]))
    r1 = l * np.dot(Kinv, H[0])
    r2 = l * np.dot(Kinv, H[1])
    r3 = np.cross(r1, r2)
    T = l * np.dot(Kinv, H[2])
    R = np.array([[r1], [r2], [r3]])
    R = np.reshape(R, (3, 3))
    U, S, V = np.linalg.svd(R, full_matrices=True)
    U = np.matrix(U)
    V = np.matrix(V)
    R = U * V
    return (R, T)
