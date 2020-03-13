import api_manager
import actor.caller as caller
import utils.settings as settings
import utils.log4py as log4py
import unittest


class Test(unittest.TestCase):
    __am = api_manager.ApiManager()
    __call = caller
    __logger = log4py.getLogger(__file__, level=settings.DEBUG_LEVEL)
    __file_list = ['강원도.txt']
    __answer = [{'documents': [{'address': {'address_name': '강원 강릉시 강동면 심곡리 20', 'b_code': '4215034029', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '20', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 심곡리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '129.051594222091', 'y': '37.6692864711714', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 심곡리 20', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '129.051594222091', 'y': '37.6692864711714'}, {'address': {'address_name': '강원 강릉시 강동면 임곡리 20', 'b_code': '4215034025', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '20', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 임곡리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.992092081113', 'y': '37.6969282757675', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 임곡리 20', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.992092081113', 'y': '37.6969282757675'}], 'meta': {'is_end': True, 'pageable_count': 2, 'total_count': 2}}, {'documents': [{'address': {'address_name': '강원 강릉시 강동면 심곡리 46', 'b_code': '4215034029', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '46', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 심곡리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '129.048329561257', 'y': '37.667611743421', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 심곡리 46', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '129.048329561257', 'y': '37.667611743421'}, {'address': {'address_name': '강원 강릉시 강동면 안인리 46', 'b_code': '4215034023', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '46', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 안인리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.981777324901', 'y': '37.7422067212921', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 안인리 46', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.981777324901', 'y': '37.7422067212921'}, {'address': {'address_name': '강원 강릉시 강동면 정동진리 46', 'b_code': '4215034028', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '46', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 정동진리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '129.039466540445', 'y': '37.685181832718', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 정동진리 46', 'address_type': 'REGION_ADDR', 'road_address': {'address_name': '강원 강릉시 강동면 헌화로 969', 'building_name': '', 'main_building_no': '969', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_name': '강동면 정동진리', 'road_name': '헌화로', 'sub_building_no': '', 'undergroun_yn': '', 'underground_yn': 'N', 'x': '129.039389654758', 'y': '37.685035786709', 'zone_no': '25631'}, 'x': '129.039466540445', 'y': '37.685181832718'}], 'meta': {'is_end': True, 'pageable_count': 3, 'total_count': 3}}, {'documents': [{'address': {'address_name': '강원 강릉시 강동면 상시동리 54', 'b_code': '4215034021', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '54', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 상시동리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.954256398315', 'y': '37.7221376536465', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 상시동리 54', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.954256398315', 'y': '37.7221376536465'}, {'address': {'address_name': '강원 강릉시 강동면 심곡리 54', 'b_code': '4215034029', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '54', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 심곡리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '129.04977339423', 'y': '37.6672148766874', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 심곡리 54', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '129.04977339423', 'y': '37.6672148766874'}, {'address': {'address_name': '강원 강릉시 강동면 언별리 54', 'b_code': '4215034031', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '54', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 언별리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.950991930149', 'y': '37.7064159505469', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 언별리 54', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.950991930149', 'y': '37.7064159505469'}, {'address': {'address_name': '강원 강릉시 강동면 임곡리 54', 'b_code': '4215034025', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '54', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 임곡리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.988546280882', 'y': '37.6959092139482', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 임곡리 54', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.988546280882', 'y': '37.6959092139482'}, {'address': {'address_name': '강원 강릉시 강동면 정동진리 54', 'b_code': '4215034028', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '54', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 정동진리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '129.039158295033', 'y': '37.6834875646506', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 정동진리 54', 'address_type': 'REGION_ADDR', 'road_address': {'address_name': '강원 강릉시 강동면 정동5길 18', 'building_name': '', 'main_building_no': '18', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_name': '강동면 정동진리', 'road_name': '정동5길', 'sub_building_no': '', 'undergroun_yn': '', 'underground_yn': 'N', 'x': '129.039174126002', 'y': '37.6834613468307', 'zone_no': '25631'}, 'x': '129.039158295033', 'y': '37.6834875646506'}, {'address': {'address_name': '강원 강릉시 강동면 하시동리 54', 'b_code': '4215034026', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '54', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 하시동리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.972403508162', 'y': '37.7373375364249', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 하시동리 54', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.972403508162', 'y': '37.7373375364249'}], 'meta': {'is_end': True, 'pageable_count': 6, 'total_count': 6}}, {'documents': [{'address': {'address_name': '강원 강릉시 강동면 상시동리 112-3', 'b_code': '4215034021', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '112', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 상시동리', 'sub_adderss_no': '', 'sub_address_no': '3', 'x': '128.950303467111', 'y': '37.7259454953002', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 상시동리 112-3', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.950303467111', 'y': '37.7259454953002'}, {'address': {'address_name': '강원 강릉시 강동면 하시동리 112-3', 'b_code': '4215034026', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '112', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 하시동리', 'sub_adderss_no': '', 'sub_address_no': '3', 'x': '128.970164645192', 'y': '37.7342851273995', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 하시동리 112-3', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.970164645192', 'y': '37.7342851273995'}], 'meta': {'is_end': True, 'pageable_count': 2, 'total_count': 2}}, {'documents': [{'address': {'address_name': '강원 강릉시 강동면 모전리 235', 'b_code': '4215034022', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '235', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 모전리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.961635569263', 'y': '37.7087039867304', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 모전리 235', 'address_type': 'REGION_ADDR', 'road_address': {'address_name': '강원 강릉시 강동면 아래장작골길 167', 'building_name': '', 'main_building_no': '167', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_name': '강동면 모전리', 'road_name': '아래장작골길', 'sub_building_no': '', 'undergroun_yn': '', 'underground_yn': 'N', 'x': '128.961705292411', 'y': '37.7085616646508', 'zone_no': '25627'}, 'x': '128.961635569263', 'y': '37.7087039867304'}, {'address': {'address_name': '강원 강릉시 강동면 산성우리 235', 'b_code': '4215034030', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '235', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 산성우리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '129.013305689429', 'y': '37.681950623521', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 산성우리 235', 'address_type': 'REGION_ADDR', 'road_address': {'address_name': '강원 강릉시 강동면 오이동길 48-10', 'building_name': '', 'main_building_no': '48', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_name': '강동면 산성우리', 'road_name': '오이동길', 'sub_building_no': '10', 'undergroun_yn': '', 'underground_yn': 'N', 'x': '129.013336191729', 'y': '37.6818756034241', 'zone_no': '25630'}, 'x': '129.013305689429', 'y': '37.681950623521'}, {'address': {'address_name': '강원 강릉시 강동면 상시동리 235', 'b_code': '4215034021', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '235', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 상시동리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.952304138907', 'y': '37.7336031852503', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 상시동리 235', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.952304138907', 'y': '37.7336031852503'}, {'address': {'address_name': '강원 강릉시 강동면 안인진리 235', 'b_code': '4215034024', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '235', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 안인진리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.982047218548', 'y': '37.7292565732355', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 안인진리 235', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.982047218548', 'y': '37.7292565732355'}, {'address': {'address_name': '강원 강릉시 강동면 언별리 235', 'b_code': '4215034031', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '235', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 언별리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.945955149791', 'y': '37.6960427691512', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 언별리 235', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.945955149791', 'y': '37.6960427691512'}, {'address': {'address_name': '강원 강릉시 강동면 임곡리 235', 'b_code': '4215034025', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '235', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 임곡리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.972677871284', 'y': '37.6870415910054', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 임곡리 235', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.972677871284', 'y': '37.6870415910054'}, {'address': {'address_name': '강원 강릉시 강동면 하시동리 235', 'b_code': '4215034026', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '235', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 하시동리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.961524057389', 'y': '37.7442731623497', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 하시동리 235', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.961524057389', 'y': '37.7442731623497'}], 'meta': {'is_end': True, 'pageable_count': 7, 'total_count': 7}}, {'documents': [{'address': {'address_name': '강원 강릉시 강동면 산성우리 167', 'b_code': '4215034030', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '167', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 산성우리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '129.012889969006', 'y': '37.6841155858322', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 산성우리 167', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '129.012889969006', 'y': '37.6841155858322'}, {'address': {'address_name': '강원 강릉시 강동면 상시동리 167', 'b_code': '4215034021', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '167', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 상시동리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.953795840943', 'y': '37.7278517437565', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 상시동리 167', 'address_type': 'REGION_ADDR', 'road_address': {'address_name': '강원 강릉시 강동면 율곡로 2210', 'building_name': '', 'main_building_no': '2210', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_name': '강동면 상시동리', 'road_name': '율곡로', 'sub_building_no': '', 'undergroun_yn': '', 'underground_yn': 'N', 'x': '128.953812542146', 'y': '37.7278614661603', 'zone_no': '25620'}, 'x': '128.953795840943', 'y': '37.7278517437565'}, {'address': {'address_name': '강원 강릉시 강동면 언별리 167', 'b_code': '4215034031', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '167', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 언별리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.94917902346', 'y': '37.6979029850337', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 언별리 167', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.94917902346', 'y': '37.6979029850337'}], 'meta': {'is_end': True, 'pageable_count': 3, 'total_count': 3}}, {'documents': [{'address': {'address_name': '강원 강릉시 강동면 정동진리 47-7', 'b_code': '4215034028', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '47', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 정동진리', 'sub_adderss_no': '', 'sub_address_no': '7', 'x': '129.039676251305', 'y': '37.6854387250587', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 정동진리 47-7', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '129.039676251305', 'y': '37.6854387250587'}], 'meta': {'is_end': True, 'pageable_count': 1, 'total_count': 1}}, {'documents': [{'address': {'address_name': '강원 강릉시 강동면 모전리 21', 'b_code': '4215034022', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '21', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 모전리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.988759440491', 'y': '37.7076267705161', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 모전리 21', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.988759440491', 'y': '37.7076267705161'}, {'address': {'address_name': '강원 강릉시 강동면 심곡리 21', 'b_code': '4215034029', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '21', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 심곡리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '129.051211155321', 'y': '37.6688083081899', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 심곡리 21', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '129.051211155321', 'y': '37.6688083081899'}, {'address': {'address_name': '강원 강릉시 강동면 안인진리 21', 'b_code': '4215034024', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '21', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 안인진리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.985835294237', 'y': '37.7379492571895', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 안인진리 21', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.985835294237', 'y': '37.7379492571895'}, {'address': {'address_name': '강원 강릉시 강동면 임곡리 21', 'b_code': '4215034025', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '21', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 임곡리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.990843217808', 'y': '37.695907916971', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 임곡리 21', 'address_type': 'REGION_ADDR', 'road_address': {'address_name': '강원 강릉시 강동면 임곡로 529-21', 'building_name': '', 'main_building_no': '529', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_name': '강동면 임곡리', 'road_name': '임곡로', 'sub_building_no': '21', 'undergroun_yn': '', 'underground_yn': 'N', 'x': '128.989304997762', 'y': '37.6953469908661', 'zone_no': '25629'}, 'x': '128.990843217808', 'y': '37.695907916971'}], 'meta': {'is_end': True, 'pageable_count': 4, 'total_count': 4}}, {'documents': [{'address': {'address_name': '강원 강릉시 강동면 산성우리 314', 'b_code': '4215034030', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '314', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 산성우리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '129.015397017955', 'y': '37.6602548801982', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 산성우리 314', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '129.015397017955', 'y': '37.6602548801982'}, {'address': {'address_name': '강원 강릉시 강동면 안인진리 314', 'b_code': '4215034024', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '314', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 안인진리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.98907160023', 'y': '37.735544037936', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 안인진리 314', 'address_type': 'REGION_ADDR', 'road_address': {'address_name': '강원 강릉시 강동면 안인진길 43', 'building_name': '', 'main_building_no': '43', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_name': '강동면 안인진리', 'road_name': '안인진길', 'sub_building_no': '', 'undergroun_yn': '', 'underground_yn': 'N', 'x': '128.989046785392', 'y': '37.7355238277541', 'zone_no': '25626'}, 'x': '128.98907160023', 'y': '37.735544037936'}, {'address': {'address_name': '강원 강릉시 강동면 언별리 314', 'b_code': '4215034031', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '314', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 언별리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.941517466144', 'y': '37.6892176351255', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 언별리 314', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.941517466144', 'y': '37.6892176351255'}, {'address': {'address_name': '강원 강릉시 강동면 임곡리 314', 'b_code': '4215034025', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '314', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 임곡리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.970067915393', 'y': '37.6801722640821', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 임곡리 314', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.970067915393', 'y': '37.6801722640821'}, {'address': {'address_name': '강원 강릉시 강동면 정동진리 314', 'b_code': '4215034028', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '314', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 정동진리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '129.032698943391', 'y': '37.6907852451725', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 정동진리 314', 'address_type': 'REGION_ADDR', 'road_address': {'address_name': '강원 강릉시 강동면 정동1길 7', 'building_name': '', 'main_building_no': '7', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_name': '강동면 정동진리', 'road_name': '정동1길', 'sub_building_no': '', 'undergroun_yn': '', 'underground_yn': 'N', 'x': '129.032700936407', 'y': '37.6907793553935', 'zone_no': '25631'}, 'x': '129.032698943391', 'y': '37.6907852451725'}, {'address': {'address_name': '강원 강릉시 강동면 하시동리 314', 'b_code': '4215034026', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '314', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 하시동리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.964683156596', 'y': '37.7391307194766', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 하시동리 314', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.964683156596', 'y': '37.7391307194766'}], 'meta': {'is_end': True, 'pageable_count': 6, 'total_count': 6}}, {'documents': [{'address': {'address_name': '강원 강릉시 강동면 산성우리 143', 'b_code': '4215034030', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '143', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 산성우리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '129.013234517149', 'y': '37.6826636798871', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 산성우리 143', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '129.013234517149', 'y': '37.6826636798871'}, {'address': {'address_name': '강원 강릉시 강동면 심곡리 143', 'b_code': '4215034029', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '143', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 심곡리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '129.051861521889', 'y': '37.6633350604641', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 심곡리 143', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '129.051861521889', 'y': '37.6633350604641'}, {'address': {'address_name': '강원 강릉시 강동면 안인리 143', 'b_code': '4215034023', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '143', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 안인리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.976430364018', 'y': '37.7370772827441', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 안인리 143', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.976430364018', 'y': '37.7370772827441'}, {'address': {'address_name': '강원 강릉시 강동면 언별리 143', 'b_code': '4215034031', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '143', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 언별리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.949716919996', 'y': '37.6969703645559', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 언별리 143', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.949716919996', 'y': '37.6969703645559'}, {'address': {'address_name': '강원 강릉시 강동면 임곡리 143', 'b_code': '4215034025', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '143', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 임곡리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.975750499816', 'y': '37.6911037325394', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 임곡리 143', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '128.975750499816', 'y': '37.6911037325394'}, {'address': {'address_name': '강원 강릉시 강동면 정동진리 143', 'b_code': '4215034028', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '143', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 정동진리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '129.034855366468', 'y': '37.686006507933', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 정동진리 143', 'address_type': 'REGION_ADDR', 'road_address': None, 'x': '129.034855366468', 'y': '37.686006507933'}, {'address': {'address_name': '강원 강릉시 강동면 하시동리 143', 'b_code': '4215034026', 'h_code': '4215034000', 'main_adderss_no': '', 'main_address_no': '143', 'mountain_yn': 'N', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_h_name': '강동면', 'region_3depth_name': '강동면 하시동리', 'sub_adderss_no': '', 'sub_address_no': '', 'x': '128.971898309626', 'y': '37.7368983671856', 'zip_code': ''}, 'address_name': '강원 강릉시 강동면 하시동리 143', 'address_type': 'REGION_ADDR', 'road_address': {'address_name': '강원 강릉시 강동면 원장봉길 36-20', 'building_name': '', 'main_building_no': '36', 'region_1depth_name': '강원', 'region_2depth_name': '강릉시', 'region_3depth_name': '강동면 하시동리', 'road_name': '원장봉길', 'sub_building_no': '20', 'undergroun_yn': '', 'underground_yn': 'N', 'x': '128.971886800986', 'y': '37.7368579321326', 'zone_no': '25620'}, 'x': '128.971898309626', 'y': '37.7368983671856'}], 'meta': {'is_end': True, 'pageable_count': 7, 'total_count': 7}}]

    def test_parallel_run(self):
        for sido in self.__file_list:
            self.__logger.debug(self.__call.parallel_run(10, 10, self.__am.makeQuery(sido)))


if __name__ == '__main__':
    unittest.main()
