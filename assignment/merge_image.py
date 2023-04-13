import cv2
import glob
import sys
import numpy
import pandas


def set_resolution(cropped_images):
    res_set = []

    for idx, img in enumerate(cropped_images):
        if idx == 0:
            stan_img_shape = img.shape[:2]
            print(stan_img_shape)
            res_set.append(img)
        else:
            if stan_img_shape == img.shape[:2]:
                print("ok")
                res_set.append(img)
            else:
                sub_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
                print(sub_img.shape[:2])
                res_set.append(sub_img)

    return res_set

def show_img(img_list):
    for idx, img in enumerate(img_list):
        cv2.imshow(f"img_{idx}", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def edge_detection(res_images, canny_images):

    # 사용되는 리스트는 res_images, canny_images
    ord_number = [i + 1 for i in range(len(res_images))]
    result_dict = []
    for i in range(len(res_images)):
        check_res = res_images.copy()
        check_canny = canny_images.copy()
        check_ord_n = ord_number.copy()
        check_res.pop(i)
        check_canny.pop(i)
        check_ord_n.pop(i)
        for res, canny, num in zip(check_res, check_canny, check_ord_n):
            # 1. hconcat

            # 1.1 orderType None
            # 1.1.1 matchingType None
            v_img = cv2.hconcat([res_images[i], res])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([canny_images[i], canny])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'none'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "none", "matchingNumber": num, "matchingType": 'Horizontal',
                 "transformation": 'none', "edgeSum": edge_sum})

            # 1.1.2 matchingType mirroring
            v_img = cv2.hconcat([res_images[i], cv2.flip(res, 1)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([canny_images[i], cv2.flip(canny, 1)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'none'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "none", "matchingNumber": num, "matchingType": 'Horizontal',
                 "transformation": 'mirroring', "edgeSum": edge_sum})

            # 1.1.3 matchingType flipping
            v_img = cv2.hconcat([res_images[i], cv2.flip(res, 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([canny_images[i], cv2.flip(canny, 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'none'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "none", "matchingNumber": num, "matchingType": 'Horizontal',
                 "transformation": 'flipping', "edgeSum": edge_sum})

            # 1.1.4 matchingType mirroring & flipping
            v_img = cv2.hconcat([res_images[i], cv2.flip(cv2.flip(res, 1), 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([canny_images[i], cv2.flip(cv2.flip(canny, 1), 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'none'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "none", "matchingNumber": num, "matchingType": 'Horizontal',
                 "transformation": 'mirroring&flipping', "edgeSum": edge_sum})

            # 1.2 orderType Mirroring
            # 1.2.1 matchingType None
            v_img = cv2.hconcat([cv2.flip(res_images[i], 1), res])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([cv2.flip(canny_images[i], 1), canny])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "mirroring", "matchingNumber": num, "matchingType": 'Horizontal',
                 "transformation": 'none', "edgeSum": edge_sum})

            # 1.2.2 matchingType mirroring
            v_img = cv2.hconcat([cv2.flip(res_images[i], 1), cv2.flip(res, 1)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([cv2.flip(canny_images[i], 1), cv2.flip(canny, 1)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "mirroring", "matchingNumber": num, "matchingType": 'Horizontal',
                 "transformation": 'mirroring', "edgeSum": edge_sum})

            # 1.2.3 matchingType flipping
            v_img = cv2.hconcat([cv2.flip(res_images[i], 1), cv2.flip(res, 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([cv2.flip(canny_images[i], 1), cv2.flip(canny, 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "mirroring", "matchingNumber": num, "matchingType": 'Horizontal',
                 "transformation": 'flipping', "edgeSum": edge_sum})

            # 1.2.4 matchingType mirroring & flipping
            v_img = cv2.hconcat([cv2.flip(res_images[i], 1), cv2.flip(cv2.flip(res, 1), 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([cv2.flip(canny_images[i], 1), cv2.flip(cv2.flip(canny, 1), 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "mirroring", "matchingNumber": num, "matchingType": 'Horizontal',
                 "transformation": 'mirroring&flipping', "edgeSum": edge_sum})

            # 1.3 orderType Flipping
            # 1.3.1 matchingType None
            v_img = cv2.hconcat([cv2.flip(res_images[i], 0), res])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([cv2.flip(canny_images[i], 0), canny])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'flipping'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "flipping", "matchingNumber": num, "matchingType": 'Horizontal',
                 "transformation": 'none', "edgeSum": edge_sum})

            # 1.3.2 matchingType mirroring
            v_img = cv2.hconcat([cv2.flip(res_images[i], 0), cv2.flip(res, 1)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([cv2.flip(canny_images[i], 0), cv2.flip(canny, 1)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'flipping'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "flipping", "matchingNumber": num, "matchingType": 'Horizontal',
                 "transformation": 'mirroring', "edgeSum": edge_sum})

            # 1.3.3 matchingType flipping
            v_img = cv2.hconcat([cv2.flip(res_images[i], 0), cv2.flip(res, 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([cv2.flip(canny_images[i], 0), cv2.flip(canny, 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'flipping'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "flipping", "matchingNumber": num, "matchingType": 'Horizontal',
                 "transformation": 'flipping', "edgeSum": edge_sum})

            # 1.3.4 matchingType mirroring & flipping
            v_img = cv2.hconcat([cv2.flip(res_images[i], 0), cv2.flip(cv2.flip(res, 1), 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([cv2.flip(canny_images[i], 0), cv2.flip(cv2.flip(canny, 1), 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'flipping'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "flipping", "matchingNumber": num, "matchingType": 'Horizontal',
                 "transformation": 'mirroring&flipping', "edgeSum": edge_sum})

            # 1.4 orderType Mirroring & Flipping
            # 1.4.1 matchingType None
            v_img = cv2.hconcat([cv2.flip(cv2.flip(res_images[i], 1), 0), res])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([cv2.flip(cv2.flip(canny_images[i], 1), 0), canny])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring&flipping'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append({"orderNumber": i + 1, "orderType": "mirroring&flipping", "matchingNumber": num,
                                "matchingType": 'Horizontal', "transformation": 'none', "edgeSum": edge_sum})

            # 1.4.2 matchingType mirroring
            v_img = cv2.hconcat([cv2.flip(cv2.flip(res_images[i], 1), 0), cv2.flip(res, 1)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([cv2.flip(cv2.flip(canny_images[i], 1), 0), cv2.flip(canny, 1)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring&flipping'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append({"orderNumber": i + 1, "orderType": "mirroring&flipping", "matchingNumber": num,
                                "matchingType": 'Horizontal', "transformation": 'mirroring', "edgeSum": edge_sum})

            # 1.4.3 matchingType flipping
            v_img = cv2.hconcat([cv2.flip(cv2.flip(res_images[i], 1), 0), cv2.flip(res, 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([cv2.flip(cv2.flip(canny_images[i], 1), 0), cv2.flip(canny, 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring&flipping'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append({"orderNumber": i + 1, "orderType": "mirroring&flipping", "matchingNumber": num,
                                "matchingType": 'Horizontal', "transformation": 'flipping', "edgeSum": edge_sum})

            # 1.4.4 matchingType mirroring & flipping
            v_img = cv2.hconcat([cv2.flip(cv2.flip(res_images[i], 1), 0), cv2.flip(cv2.flip(res, 1), 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.hconcat([cv2.flip(cv2.flip(canny_images[i], 1), 0), cv2.flip(cv2.flip(canny, 1), 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring&flipping'}Matching Order {num}, Merge Type {'Horizontal'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append({"orderNumber": i + 1, "orderType": "mirroring&flipping", "matchingNumber": num,
                                "matchingType": 'Horizontal', "transformation": 'mirroring&flipping',
                                "edgeSum": edge_sum})

            # 2. vertical

            # 2.1 orderType None
            # 2.1.1 matchingType None
            v_img = cv2.vconcat([res_images[i], res])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([canny_images[i], canny])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[int(h / 2 - 30):int(h / 2 + 30), :])
            print(
                f"Order Number {i + 1}, orderType: {'none'}, Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "none", "matchingNumber": num, "matchingType": 'vertical',
                 "transformation": 'none', "edgeSum": edge_sum})

            # 2.1.2 matchingType mirroring
            v_img = cv2.vconcat([res_images[i], cv2.flip(res, 1)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([canny_images[i], cv2.flip(canny, 1)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[int(h / 2 - 30):int(h / 2 + 30), :])
            print(
                f"Order Number {i + 1}, orderType: {'none'}Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "none", "matchingNumber": num, "matchingType": 'vertical',
                 "transformation": 'mirroring', "edgeSum": edge_sum})

            # 2.1.3 matchingType flipping
            v_img = cv2.vconcat([res_images[i], cv2.flip(res, 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([canny_images[i], cv2.flip(canny, 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[int(h / 2 - 30):int(h / 2 + 30), :])
            print(
                f"Order Number {i + 1}, orderType: {'none'}Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "none", "matchingNumber": num, "matchingType": 'vertical',
                 "transformation": 'flipping', "edgeSum": edge_sum})

            # 2.1.4 matchingType mirroring & flipping
            v_img = cv2.vconcat([res_images[i], cv2.flip(cv2.flip(res, 1), 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([canny_images[i], cv2.flip(cv2.flip(canny, 1), 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[int(h / 2 - 30):int(h / 2 + 30), :])
            print(
                f"Order Number {i + 1}, orderType: {'none'}Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "none", "matchingNumber": num, "matchingType": 'vertical',
                 "transformation": 'mirroring&flipping', "edgeSum": edge_sum})

            # 2.2 orderType Mirroring
            # 2.2.1 matchingType None
            v_img = cv2.vconcat([cv2.flip(res_images[i], 1), res])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([cv2.flip(canny_images[i], 1), canny])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[int(h / 2 - 30):int(h / 2 + 30), :])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring'}Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "mirroring", "matchingNumber": num, "matchingType": 'vertical',
                 "transformation": 'none', "edgeSum": edge_sum})

            # 2.2.2 matchingType mirroring
            v_img = cv2.vconcat([cv2.flip(res_images[i], 1), cv2.flip(res, 1)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([cv2.flip(canny_images[i], 1), cv2.flip(canny, 1)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[int(h / 2 - 30):int(h / 2 + 30), :])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring'}Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "mirroring", "matchingNumber": num, "matchingType": 'vertical',
                 "transformation": 'mirroring', "edgeSum": edge_sum})

            # 2.2.3 matchingType flipping
            v_img = cv2.vconcat([cv2.flip(res_images[i], 1), cv2.flip(res, 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([cv2.flip(canny_images[i], 1), cv2.flip(canny, 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[int(h / 2 - 30):int(h / 2 + 30), :])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring'}Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "mirroring", "matchingNumber": num, "matchingType": 'vertical',
                 "transformation": 'flipping', "edgeSum": edge_sum})

            # 2.2.4 matchingType mirroring & flipping
            v_img = cv2.vconcat([cv2.flip(res_images[i], 1), cv2.flip(cv2.flip(res, 1), 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([cv2.flip(canny_images[i], 1), cv2.flip(cv2.flip(canny, 1), 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[int(h / 2 - 30):int(h / 2 + 30), :])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring'}Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "mirroring", "matchingNumber": num, "matchingType": 'vertical',
                 "transformation": 'mirroring&flipping', "edgeSum": edge_sum})

            # 2.3 orderType Flipping
            # 2.3.1 matchingType None
            v_img = cv2.vconcat([cv2.flip(res_images[i], 0), res])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([cv2.flip(canny_images[i], 0), canny])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[int(h / 2 - 30):int(h / 2 + 30), :])
            print(
                f"Order Number {i + 1}, orderType: {'flipping'}Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "flipping", "matchingNumber": num, "matchingType": 'vertical',
                 "transformation": 'none', "edgeSum": edge_sum})

            # 2.3.2 matchingType mirroring
            v_img = cv2.vconcat([cv2.flip(res_images[i], 0), cv2.flip(res, 1)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([cv2.flip(canny_images[i], 0), cv2.flip(canny, 1)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[:, int(w / 2 - 30):int(w / 2 + 30)])
            print(
                f"Order Number {i + 1}, orderType: {'flipping'}Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "flipping", "matchingNumber": num, "matchingType": 'vertical',
                 "transformation": 'mirroring', "edgeSum": edge_sum})

            # 2.3.3 matchingType flipping
            v_img = cv2.vconcat([cv2.flip(res_images[i], 0), cv2.flip(res, 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([cv2.flip(canny_images[i], 0), cv2.flip(canny, 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[int(h / 2 - 30):int(h / 2 + 30), :])
            print(
                f"Order Number {i + 1}, orderType: {'flipping'}Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "flipping", "matchingNumber": num, "matchingType": 'vertical',
                 "transformation": 'flipping', "edgeSum": edge_sum})

            # 2.3.4 matchingType mirroring & flipping
            v_img = cv2.vconcat([cv2.flip(res_images[i], 0), cv2.flip(cv2.flip(res, 1), 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([cv2.flip(canny_images[i], 0), cv2.flip(cv2.flip(canny, 1), 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[int(h / 2 - 30):int(h / 2 + 30), :])
            print(
                f"Order Number {i + 1}, orderType: {'flipping'}Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append(
                {"orderNumber": i + 1, "orderType": "flipping", "matchingNumber": num, "matchingType": 'vertical',
                 "transformation": 'mirroring&flipping', "edgeSum": edge_sum})

            # 2.4 orderType Mirroring & Flipping
            # 2.4.1 matchingType None
            v_img = cv2.vconcat([cv2.flip(cv2.flip(res_images[i], 1), 0), res])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([cv2.flip(cv2.flip(canny_images[i], 1), 0), canny])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[int(h / 2 - 30):int(h / 2 + 30), :])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring&flipping'}Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append({"orderNumber": i + 1, "orderType": "mirroring&flipping", "matchingNumber": num,
                                "matchingType": 'vertical', "transformation": 'none', "edgeSum": edge_sum})

            # 2.4.2 matchingType mirroring
            v_img = cv2.vconcat([cv2.flip(cv2.flip(res_images[i], 1), 0), cv2.flip(res, 1)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([cv2.flip(cv2.flip(canny_images[i], 1), 0), cv2.flip(canny, 1)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[int(h / 2 - 30):int(h / 2 + 30), :])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring&flipping'}Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append({"orderNumber": i + 1, "orderType": "mirroring&flipping", "matchingNumber": num,
                                "matchingType": 'vertical', "transformation": 'mirroring', "edgeSum": edge_sum})

            # 2.4.3 matchingType flipping
            v_img = cv2.vconcat([cv2.flip(cv2.flip(res_images[i], 1), 0), cv2.flip(res, 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([cv2.flip(cv2.flip(canny_images[i], 1), 0), cv2.flip(canny, 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[int(h / 2 - 30):int(h / 2 + 30), :])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring&flipping'}Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append({"orderNumber": i + 1, "orderType": "mirroring&flipping", "matchingNumber": num,
                                "matchingType": 'vertical', "transformation": 'flipping', "edgeSum": edge_sum})

            # 2.4.4 matchingType mirroring & flipping
            v_img = cv2.vconcat([cv2.flip(cv2.flip(res_images[i], 1), 0), cv2.flip(cv2.flip(res, 1), 0)])
            v_canny_img = cv2.Canny(v_img, 60, 200)
            v_c_img = cv2.vconcat([cv2.flip(cv2.flip(canny_images[i], 1), 0), cv2.flip(cv2.flip(canny, 1), 0)])
            diff_img = v_canny_img - v_c_img
            h, w = v_img.shape[:2]
            edge_sum = numpy.sum(diff_img[int(h / 2 - 30):int(h / 2 + 30), :])
            print(
                f"Order Number {i + 1}, orderType: {'mirroring&flipping'}Matching Order {num}, Merge Type {'vertical'}, Transformation {'none'} , EdgeSum {edge_sum}")
            result_dict.append({"orderNumber": i + 1, "orderType": "mirroring&flipping", "matchingNumber": num,
                                "matchingType": 'vertical', "transformation": 'mirroring&flipping',
                                "edgeSum": edge_sum})

    return pandas.DataFrame(result_dict)

if __name__ == "__main__":

    cols, rows = sys.argv[1], sys.argv[2]

    cropped_images = [cv2.imread(f) for f in glob.glob("image/crooped_images/*.jpg")]

    # Gray Scale 변환
    processed_img = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in cropped_images]

    # Gaussian Blur
    processed_img = [cv2.GaussianBlur(img, (0, 0), 2) for img in processed_img]

    # image resolution 통일(90degree rotation 해결)
    res_images = set_resolution(processed_img)

    # canny Edge Detection
    canny_images = [cv2.Canny(img, 60, 200) for img in res_images]

    # 각 이미지의 변환 형태에 따른 Edge를 검출하여 경계선 부분의 edge 합을 구하는 코드
    df = edge_detection(res_images, canny_images)
