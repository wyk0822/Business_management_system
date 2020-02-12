/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : wx_Project

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2020-01-02 16:45:50
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add group', '2', 'add_group');
INSERT INTO `auth_permission` VALUES ('5', 'Can change group', '2', 'change_group');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete group', '2', 'delete_group');
INSERT INTO `auth_permission` VALUES ('7', 'Can add permission', '3', 'add_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can change permission', '3', 'change_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete permission', '3', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add 商品类别', '7', 'add_goods_types');
INSERT INTO `auth_permission` VALUES ('20', 'Can change 商品类别', '7', 'change_goods_types');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete 商品类别', '7', 'delete_goods_types');
INSERT INTO `auth_permission` VALUES ('22', 'Can add 订单详情', '8', 'add_order');
INSERT INTO `auth_permission` VALUES ('23', 'Can change 订单详情', '8', 'change_order');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete 订单详情', '8', 'delete_order');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 商品信息', '9', 'add_goods');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 商品信息', '9', 'change_goods');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 商品信息', '9', 'delete_goods');
INSERT INTO `auth_permission` VALUES ('28', 'Can add 管理员信息', '10', 'add_administrators');
INSERT INTO `auth_permission` VALUES ('29', 'Can change 管理员信息', '10', 'change_administrators');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete 管理员信息', '10', 'delete_administrators');
INSERT INTO `auth_permission` VALUES ('31', 'Can add 购买人信息', '11', 'add_buy_peoples');
INSERT INTO `auth_permission` VALUES ('32', 'Can change 购买人信息', '11', 'change_buy_peoples');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete 购买人信息', '11', 'delete_buy_peoples');
INSERT INTO `auth_permission` VALUES ('34', 'Can add cart', '12', 'add_cart');
INSERT INTO `auth_permission` VALUES ('35', 'Can change cart', '12', 'change_cart');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete cart', '12', 'delete_cart');
INSERT INTO `auth_permission` VALUES ('37', 'Can add captcha store', '13', 'add_captchastore');
INSERT INTO `auth_permission` VALUES ('38', 'Can change captcha store', '13', 'change_captchastore');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete captcha store', '13', 'delete_captchastore');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$36000$qOYxnjOhVLBN$hiBhdoRAywsjskdXMZCjqsWxb9rVIFZt13cZReCNbeE=', '2019-04-15 14:00:29.622493', '1', 'python', '', '', 'QE@12.com', '1', '1', '2019-01-25 04:06:29.315201');
INSERT INTO `auth_user` VALUES ('2', 'pbkdf2_sha256$36000$EbYDZRllTpNw$PasWDd/AqdIMMd5Ko/Hn1+fqd6qZYs2C6z+bnKzpk74=', '2019-02-25 10:12:56.128794', '0', 'python1', '张三', '张', '123@123.cn', '1', '1', '2019-02-25 10:08:00.000000');

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `buy_peoples`
-- ----------------------------
DROP TABLE IF EXISTS `buy_peoples`;
CREATE TABLE `buy_peoples` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `buy_people_name` varchar(50) NOT NULL,
  `buy_people_alljifen` decimal(10,2) NOT NULL,
  `buy_people_keyongjifen` decimal(10,2) NOT NULL,
  `buy_people_allmoney` decimal(10,2) NOT NULL,
  `buy_people_phone` varchar(11) NOT NULL,
  `buy_people_addr` longtext NOT NULL,
  `buy_people_age` varchar(20) NOT NULL,
  `buy_people_sex` varchar(20) NOT NULL,
  `buy_people_is_show` tinyint(1) NOT NULL,
  `administrator_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `buy_peoples_administrator_id_id_928568c4_fk_super_user_id` (`administrator_id_id`),
  CONSTRAINT `buy_peoples_administrator_id_id_928568c4_fk_super_user_id` FOREIGN KEY (`administrator_id_id`) REFERENCES `super_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of buy_peoples
-- ----------------------------
INSERT INTO `buy_peoples` VALUES ('1', '张三', '514.73', '1999790.09', '50367.50', '18888888888', '暂无', 'a', 'a', '1', '1');
INSERT INTO `buy_peoples` VALUES ('2', '李四', '1944.11', '744.00', '192188.50', '18888888888', '暂无', 'a', 'a', '1', '1');
INSERT INTO `buy_peoples` VALUES ('3', '王五', '0.00', '0.00', '0.00', '18888888888', '暂无', 'a', 'a', '0', '1');
INSERT INTO `buy_peoples` VALUES ('4', '666', '0.00', '0.00', '0.00', '11111111111', '暂无', 'b', 'a', '1', '1');

-- ----------------------------
-- Table structure for `captcha_captchastore`
-- ----------------------------
DROP TABLE IF EXISTS `captcha_captchastore`;
CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB AUTO_INCREMENT=6111 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of captcha_captchastore
-- ----------------------------
INSERT INTO `captcha_captchastore` VALUES ('6005', 'TSGM', 'tsgm', 'dbb5b19d786b9de7ad9807edc83466d0386b1763', '2019-12-03 16:44:24.321142');
INSERT INTO `captcha_captchastore` VALUES ('6006', 'EHTG', 'ehtg', '5dac92d7352ac75b448d68fa32b49d9b225e2b32', '2019-12-03 16:44:24.999669');
INSERT INTO `captcha_captchastore` VALUES ('6007', 'YKNN', 'yknn', 'e1b5368614ac1f423d14cbaa35b80c0eb9024a1f', '2019-12-03 16:44:25.212875');
INSERT INTO `captcha_captchastore` VALUES ('6008', 'VZKI', 'vzki', '2459b5150b0e8a2dd1ef7e14371c27abc32f259d', '2019-12-03 16:44:25.451972');
INSERT INTO `captcha_captchastore` VALUES ('6009', 'WYVV', 'wyvv', '2f6721aa8dadd628b40e2e3588de8cb955ed9ebe', '2019-12-03 16:44:25.495649');
INSERT INTO `captcha_captchastore` VALUES ('6010', 'JWPQ', 'jwpq', '1c279a6c19e62ab2685e08c580656071d484e6e0', '2019-12-03 16:44:25.779491');
INSERT INTO `captcha_captchastore` VALUES ('6011', 'FMVY', 'fmvy', '3ebb6922901431cd843e1f5ee5e081ce0bb47ce1', '2019-12-03 16:44:25.756919');
INSERT INTO `captcha_captchastore` VALUES ('6012', 'PCPC', 'pcpc', 'edf0eea99d8d7e6b925267b09729443536a35ce0', '2019-12-03 16:44:25.906046');
INSERT INTO `captcha_captchastore` VALUES ('6013', 'PEDQ', 'pedq', 'caa4fd2af86315f915adbe3b0d086719d5e71f3a', '2019-12-03 17:31:12.449108');
INSERT INTO `captcha_captchastore` VALUES ('6014', 'BTQC', 'btqc', '712cbf1c3987c776b6821fa69896fb0452667c21', '2019-12-03 17:31:54.843780');
INSERT INTO `captcha_captchastore` VALUES ('6015', 'BSKH', 'bskh', '7b9dbf3e88775f62a759ffa6c9e15286154bcd02', '2019-12-03 17:31:55.943531');
INSERT INTO `captcha_captchastore` VALUES ('6016', 'NXFZ', 'nxfz', 'e5fb8eddf9e3209ab5f516c9fc93faf3ef6544c3', '2019-12-03 17:31:56.710344');
INSERT INTO `captcha_captchastore` VALUES ('6017', 'NHPJ', 'nhpj', '6872eae6fc0168b7a0a83e8cc46709b23b4aec9c', '2019-12-05 14:02:15.540833');
INSERT INTO `captcha_captchastore` VALUES ('6018', 'FSUZ', 'fsuz', '36a2c0352f0150498547687feaedef1718bf4602', '2019-12-05 14:02:26.570643');
INSERT INTO `captcha_captchastore` VALUES ('6019', 'VDDY', 'vddy', '8fe81fb2b512d95c4d8fb84789869f0c77c5216e', '2019-12-05 14:03:01.152706');
INSERT INTO `captcha_captchastore` VALUES ('6020', 'UCUN', 'ucun', '2b28cf264c0503d75e9ab1de6623d7f0679668cc', '2019-12-05 14:03:02.191624');
INSERT INTO `captcha_captchastore` VALUES ('6021', 'FOZI', 'fozi', '377502dcdbbca5140947c9cf03dd91fd31539acd', '2019-12-05 14:03:10.920323');
INSERT INTO `captcha_captchastore` VALUES ('6022', 'YDBU', 'ydbu', '1048fb1e75d94a585db62a064dc60bb24c57a046', '2019-12-05 14:16:02.343309');
INSERT INTO `captcha_captchastore` VALUES ('6023', 'WWXN', 'wwxn', '8a553866b33997104172497bc8fe23f08bdf38ce', '2019-12-05 14:16:04.713239');
INSERT INTO `captcha_captchastore` VALUES ('6024', 'WBJI', 'wbji', '3926372533e60b73eeb497cab5502e90a54a3a98', '2019-12-05 14:16:34.227284');
INSERT INTO `captcha_captchastore` VALUES ('6025', 'BBCM', 'bbcm', '2f9ceab125f4cd718903794a8111e91cad6ee0b1', '2019-12-05 14:16:36.041885');
INSERT INTO `captcha_captchastore` VALUES ('6026', 'MLFJ', 'mlfj', '6bea8bd00f3960d1df0a9e3f3c1d83480966010e', '2019-12-05 14:16:36.829267');
INSERT INTO `captcha_captchastore` VALUES ('6027', 'UQSG', 'uqsg', '661e72415d8fa699e8bafa9bcb20e4bc721d28be', '2019-12-05 14:16:37.345018');
INSERT INTO `captcha_captchastore` VALUES ('6028', 'UFCO', 'ufco', 'cbdbb0211b67a1e742d21893c0409d7e5a9af686', '2019-12-05 14:17:39.399617');
INSERT INTO `captcha_captchastore` VALUES ('6029', 'KFKY', 'kfky', '37c2ff0164122025f73b16c58ca2d56a671c2b73', '2019-12-05 14:17:44.221621');
INSERT INTO `captcha_captchastore` VALUES ('6030', 'OHNX', 'ohnx', '7b85146752db2137b7f70b1417b24832885a27da', '2019-12-05 14:21:46.793099');
INSERT INTO `captcha_captchastore` VALUES ('6031', 'YYJC', 'yyjc', '772604de488f487898601bc72dfb246614a1365b', '2019-12-05 14:21:48.609019');
INSERT INTO `captcha_captchastore` VALUES ('6032', 'QIPG', 'qipg', 'f2536d1fc387cd787984193a0c65aef8665f7aa4', '2019-12-05 14:21:58.111842');
INSERT INTO `captcha_captchastore` VALUES ('6033', 'AHTT', 'ahtt', '1f7cb8b3114aee96a38d87c38d83d223e4148a6a', '2019-12-05 14:21:58.635416');
INSERT INTO `captcha_captchastore` VALUES ('6034', 'ZXHW', 'zxhw', '2cf6a5fea10b46dbbf829770e89a6c2c6266479c', '2019-12-05 14:21:59.008497');
INSERT INTO `captcha_captchastore` VALUES ('6035', 'AJRH', 'ajrh', '0a55cbcb79732d3df40a1db822aaa94fe80cc798', '2019-12-05 14:21:59.251617');
INSERT INTO `captcha_captchastore` VALUES ('6036', 'PJCY', 'pjcy', 'accc476fdc86fe63c7939b3883c6a697fc6f0311', '2019-12-05 14:23:07.273137');
INSERT INTO `captcha_captchastore` VALUES ('6037', 'JTCV', 'jtcv', 'bba70422c12dc2261490bf394d7891c747598097', '2019-12-05 14:23:10.173042');
INSERT INTO `captcha_captchastore` VALUES ('6038', 'RWUU', 'rwuu', '0d94053eb49344cdaf46e1b8c35d2a4a1452eb5d', '2019-12-05 14:23:10.941767');
INSERT INTO `captcha_captchastore` VALUES ('6039', 'FJJB', 'fjjb', 'f1a0f4f4c813cd617376a577b568dc05d87268e1', '2019-12-05 14:23:11.131658');
INSERT INTO `captcha_captchastore` VALUES ('6040', 'MWLH', 'mwlh', 'fd295499e496c943aaf63b5c3bbe1aa533c89375', '2019-12-05 14:23:11.491347');
INSERT INTO `captcha_captchastore` VALUES ('6041', 'PKPP', 'pkpp', 'ffdf20a3e751a1c750655fddf12ae7d7dac95966', '2019-12-05 14:23:11.663926');
INSERT INTO `captcha_captchastore` VALUES ('6042', 'HUBX', 'hubx', '3860a7f7ff24c7199ea3c7e48e5f9f265aafc8d3', '2019-12-05 14:23:11.842669');
INSERT INTO `captcha_captchastore` VALUES ('6043', 'PFDC', 'pfdc', '6df221456806d4fa12e7abd0d15961dee8a467a5', '2019-12-05 14:23:12.042230');
INSERT INTO `captcha_captchastore` VALUES ('6044', 'ZSPL', 'zspl', '1f04e9fbec10468e460ff944297aed3b76d53731', '2019-12-05 14:29:13.962075');
INSERT INTO `captcha_captchastore` VALUES ('6045', 'JTJS', 'jtjs', 'b6db33886248f34d42a88a497586a7aadd42f65b', '2019-12-05 14:29:20.351304');
INSERT INTO `captcha_captchastore` VALUES ('6046', 'WQFS', 'wqfs', '1980a4c90e2cd44b5b414a835e00819fef4e1c54', '2019-12-05 14:38:15.949214');
INSERT INTO `captcha_captchastore` VALUES ('6047', 'VQFY', 'vqfy', '7269ce7b2c05e2320106b0d522393deefa35ac3f', '2019-12-05 14:38:19.105050');
INSERT INTO `captcha_captchastore` VALUES ('6048', 'QNOX', 'qnox', '2aae46e53220efb989a1e328d2e2ba3f3e1288e0', '2019-12-05 14:38:19.165128');
INSERT INTO `captcha_captchastore` VALUES ('6049', 'XEBP', 'xebp', '542b4402579c0b43921f9cbc38e37c7e045ef68e', '2019-12-05 14:38:37.837776');
INSERT INTO `captcha_captchastore` VALUES ('6050', 'ACKH', 'ackh', '4f2299bf1cf44796a4f7a7e5474aeab71d9f8c45', '2019-12-05 14:38:39.309217');
INSERT INTO `captcha_captchastore` VALUES ('6051', 'MXWF', 'mxwf', '5774470f6a8122f52260d6d79d919f4cf69ec2c9', '2019-12-05 14:38:39.538862');
INSERT INTO `captcha_captchastore` VALUES ('6052', 'FLVB', 'flvb', '00bb8b901556124885d25b2e97c4cc4cd41dd652', '2019-12-05 14:38:39.744946');
INSERT INTO `captcha_captchastore` VALUES ('6053', 'OARM', 'oarm', 'cab469c65b146ecba15d4f757b6496c69fba40e0', '2019-12-05 14:53:21.686412');
INSERT INTO `captcha_captchastore` VALUES ('6054', 'SDYI', 'sdyi', '24778bd08e55aa80e745285afbf681535241ce7f', '2019-12-05 14:53:24.445048');
INSERT INTO `captcha_captchastore` VALUES ('6055', 'QYNP', 'qynp', '15fb54a93667073f0e5cb76c7850f8f4e8d8222e', '2019-12-05 14:53:30.370767');
INSERT INTO `captcha_captchastore` VALUES ('6056', 'LSAM', 'lsam', '0ae71af22eac8cb83a687fff8e525c78f922489a', '2019-12-05 14:53:46.749183');
INSERT INTO `captcha_captchastore` VALUES ('6057', 'XGHB', 'xghb', '1d9fb05149518cae25940920a94eb66f9095b03e', '2019-12-05 14:54:39.074523');
INSERT INTO `captcha_captchastore` VALUES ('6058', 'JXXE', 'jxxe', 'b31690cf09787cf1d66a647cecb5d6f976bbfdcf', '2019-12-05 14:54:41.462576');
INSERT INTO `captcha_captchastore` VALUES ('6059', 'ZDIW', 'zdiw', 'fe21c6de979e38c5b96c3ba4346d8e89bd4c23b8', '2019-12-05 14:55:09.115976');
INSERT INTO `captcha_captchastore` VALUES ('6060', 'FQXD', 'fqxd', 'c79aa10c0eebf526b7a581516fe772ef8fcb771e', '2019-12-05 14:55:10.940873');
INSERT INTO `captcha_captchastore` VALUES ('6061', 'DJDD', 'djdd', '6440efc3c56917f9d9b2fb62db459e6d5618a3f4', '2019-12-05 15:00:58.907768');
INSERT INTO `captcha_captchastore` VALUES ('6062', 'NGYI', 'ngyi', '0ed98379ba6a53c665743e6cbc3b1c14fdc37ac7', '2019-12-05 15:01:01.033915');
INSERT INTO `captcha_captchastore` VALUES ('6063', 'TKOY', 'tkoy', '4878d15fdf636b216c73aec985b56bd30693cab2', '2019-12-05 15:01:01.089997');
INSERT INTO `captcha_captchastore` VALUES ('6064', 'NCHR', 'nchr', 'e79bba8f69239d6f5c66a3bcc0510cbd9bbab132', '2019-12-05 15:01:05.733321');
INSERT INTO `captcha_captchastore` VALUES ('6065', 'GJAH', 'gjah', '57edce93183e1e4772482f4ce482c25855f59b42', '2019-12-05 15:01:05.784223');
INSERT INTO `captcha_captchastore` VALUES ('6066', 'PYPV', 'pypv', '58e7937c5dfc9fd7dc2531630c23c534006a24bc', '2019-12-05 15:01:06.773883');
INSERT INTO `captcha_captchastore` VALUES ('6067', 'KAZS', 'kazs', 'a0d42955138635be7c133072c738b9f7731d3d43', '2019-12-05 15:01:06.915018');
INSERT INTO `captcha_captchastore` VALUES ('6068', 'BIGX', 'bigx', '0bdfff8d3917e1f5962b0d42299d4b015e8996a4', '2019-12-05 15:02:36.251940');
INSERT INTO `captcha_captchastore` VALUES ('6069', 'XNGJ', 'xngj', '272b09ee2cc2635629bf77ab145f772312b67c23', '2019-12-05 15:02:48.528193');
INSERT INTO `captcha_captchastore` VALUES ('6070', 'WYJC', 'wyjc', '369b46eade3fbfa1165780ddc370e1b8aa9ca574', '2019-12-05 15:02:48.724274');
INSERT INTO `captcha_captchastore` VALUES ('6071', 'ANZW', 'anzw', 'ce59cda60a797b94bdbc78c299bcf3bd31bc184c', '2019-12-05 16:48:09.898527');
INSERT INTO `captcha_captchastore` VALUES ('6072', 'CFBA', 'cfba', 'fefb778787d7e50f40ffc7b4d6ef63806c726db2', '2019-12-05 16:48:16.377493');
INSERT INTO `captcha_captchastore` VALUES ('6073', 'PJAD', 'pjad', '535d586c2cd3a3bbc53e489f40ebe50d074d57c2', '2019-12-05 16:48:28.136128');
INSERT INTO `captcha_captchastore` VALUES ('6074', 'JGYJ', 'jgyj', 'd2a4ff299a92307087400a1737ec5387e12990ad', '2019-12-05 16:48:29.442162');
INSERT INTO `captcha_captchastore` VALUES ('6075', 'DHWG', 'dhwg', 'b54981b3dee1b3334ef16b4251cc366fe1b9dd8e', '2019-12-05 16:48:52.171734');
INSERT INTO `captcha_captchastore` VALUES ('6076', 'LBKW', 'lbkw', '01db037bfba11bda8e6edadd5fb961dc24150440', '2019-12-05 16:49:03.181256');
INSERT INTO `captcha_captchastore` VALUES ('6077', 'RHQJ', 'rhqj', '39717de565e1bdf0a2bb5406a9abe8b36d108933', '2019-12-05 16:49:03.332988');
INSERT INTO `captcha_captchastore` VALUES ('6078', 'AMHJ', 'amhj', 'a9c4b1c52d944bf18975ee507cb0ef1132bd8edd', '2019-12-05 17:00:11.432239');
INSERT INTO `captcha_captchastore` VALUES ('6079', 'HUWV', 'huwv', '7e7316db5242992ddb25121c0d1e4a500aba6a1c', '2019-12-05 17:20:12.167154');
INSERT INTO `captcha_captchastore` VALUES ('6080', 'QHKG', 'qhkg', '2d027ec752dd07c135e0b8dec245bcc22db3ae77', '2019-12-05 17:20:13.581629');
INSERT INTO `captcha_captchastore` VALUES ('6081', 'MXCE', 'mxce', 'fd3fafd51ff0c45365f256961a559fd2a984b752', '2019-12-05 17:20:13.709076');
INSERT INTO `captcha_captchastore` VALUES ('6082', 'WSQY', 'wsqy', '53a05e99b9c32350a8887fdac770ba7d1b00821b', '2019-12-05 17:21:08.305371');
INSERT INTO `captcha_captchastore` VALUES ('6083', 'LQWA', 'lqwa', 'd2302e2b5fe1f818c7fa2cf9a20f672152cc117e', '2019-12-05 17:21:21.571136');
INSERT INTO `captcha_captchastore` VALUES ('6084', 'JQWR', 'jqwr', '08eee5c7d5aa303b303953fa101e1f659cb0da39', '2019-12-05 17:21:21.922156');
INSERT INTO `captcha_captchastore` VALUES ('6085', 'GRDY', 'grdy', '9028f62ee9c1a3ffcf90ac2bf3fa5d26f3ef5ae8', '2019-12-05 17:23:42.232933');
INSERT INTO `captcha_captchastore` VALUES ('6086', 'AYWT', 'aywt', 'd9d266eb711a9b1a4774a843dc218bd96d9a64e0', '2019-12-05 17:23:43.885706');
INSERT INTO `captcha_captchastore` VALUES ('6087', 'FTRR', 'ftrr', 'ac21d661f46c04a9549dfc56a8ce297b8a4203d8', '2019-12-05 17:23:48.003889');
INSERT INTO `captcha_captchastore` VALUES ('6088', 'QMPG', 'qmpg', '253830e089884a47a3d82d2da56c4eba5a899ba1', '2019-12-05 17:23:48.355225');
INSERT INTO `captcha_captchastore` VALUES ('6089', 'TSEA', 'tsea', '7572b9c9a5e4f5fd86c79649ec4c6ca96b74f162', '2019-12-05 17:26:40.600630');
INSERT INTO `captcha_captchastore` VALUES ('6090', 'RJMH', 'rjmh', 'd9f2f296176eb1995a6a9422f326a1a7fe8147ee', '2019-12-05 17:26:41.892573');
INSERT INTO `captcha_captchastore` VALUES ('6091', 'TEPH', 'teph', 'b15d6f3b9296edffc2e25a62a45e234901ce1c48', '2019-12-05 17:26:42.986681');
INSERT INTO `captcha_captchastore` VALUES ('6092', 'OXMT', 'oxmt', 'e7f869cf2549674e8821b5991edf1c1ff8fa97ac', '2019-12-05 17:26:43.710122');
INSERT INTO `captcha_captchastore` VALUES ('6093', 'RSGA', 'rsga', 'a606c03110e32b9354a10897c506155bf6a0d5dc', '2019-12-05 17:26:44.249961');
INSERT INTO `captcha_captchastore` VALUES ('6094', 'JZZP', 'jzzp', '082b18c7a4728f40e5fe89579bef5d8f3b880d5b', '2019-12-05 17:26:52.760974');
INSERT INTO `captcha_captchastore` VALUES ('6095', 'YBNC', 'ybnc', '04355b90ce38ce70010d2b0a5a1da0f5cfc67364', '2019-12-05 17:26:53.423818');
INSERT INTO `captcha_captchastore` VALUES ('6096', 'GEOX', 'geox', '1d4673cfdbad98f92da88e6608ed862229d11681', '2019-12-05 17:26:53.988161');
INSERT INTO `captcha_captchastore` VALUES ('6097', 'DQEF', 'dqef', '13587098c252f454d31003fa57d43e6f176e3ea8', '2019-12-05 17:26:54.729319');
INSERT INTO `captcha_captchastore` VALUES ('6098', 'YHHT', 'yhht', 'e690197112edf775cf6e3010e988ec814fd1f32c', '2019-12-05 17:26:55.251685');
INSERT INTO `captcha_captchastore` VALUES ('6099', 'ISBG', 'isbg', 'd1243786bf58d36c2e780171efb5b0fb4b10fee7', '2019-12-05 17:26:55.720350');
INSERT INTO `captcha_captchastore` VALUES ('6100', 'PKEZ', 'pkez', 'b61323912498c5f6b370133d7ec0db0d73929d38', '2019-12-05 17:26:56.839197');
INSERT INTO `captcha_captchastore` VALUES ('6101', 'OEDB', 'oedb', '396ff66ef0a3e36f62a45c39844d7db7d5aec39c', '2019-12-05 17:26:57.638904');
INSERT INTO `captcha_captchastore` VALUES ('6102', 'HTHP', 'hthp', 'a931701094b06ebd2811af7c5e81e9cf14fd91b7', '2019-12-05 17:27:08.345199');
INSERT INTO `captcha_captchastore` VALUES ('6103', 'EBVE', 'ebve', 'd15e2ab9230ee57637894c16fe900809adb39797', '2019-12-05 17:27:09.495671');
INSERT INTO `captcha_captchastore` VALUES ('6104', 'LCUI', 'lcui', 'b4b6fd94f9d6fa5d9ceee551c540d83355ecbf97', '2019-12-05 17:27:10.215919');
INSERT INTO `captcha_captchastore` VALUES ('6105', 'GUSC', 'gusc', 'c56ec268fb6b7c107c618a9e532e3a1050639c40', '2019-12-05 17:27:12.217767');
INSERT INTO `captcha_captchastore` VALUES ('6106', 'SXDF', 'sxdf', 'cf0471f0c2abffb2358d8bc7be021a3598b47d28', '2019-12-14 15:28:43.920435');
INSERT INTO `captcha_captchastore` VALUES ('6107', 'ACXC', 'acxc', '37f32949b6dfff547ac67da7c33dddcdcaf2946d', '2019-12-31 11:08:17.286853');
INSERT INTO `captcha_captchastore` VALUES ('6108', 'SCBY', 'scby', '1ef99bbb92cf853bfdd00d621def0b420720bdfb', '2020-01-02 15:17:53.146764');
INSERT INTO `captcha_captchastore` VALUES ('6109', 'DEKF', 'dekf', '692e88b51542fc6c39948767c285c383790f3580', '2020-01-02 15:37:05.781024');
INSERT INTO `captcha_captchastore` VALUES ('6110', 'ACKH', 'ackh', 'ced51d933827448c8b10d42af5bca33e8e8a989c', '2020-01-02 15:38:13.975846');

-- ----------------------------
-- Table structure for `cart`
-- ----------------------------
DROP TABLE IF EXISTS `cart`;
CREATE TABLE `cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `count` int(11) NOT NULL,
  `goods_id_id` int(11) NOT NULL,
  `order_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userInfo_cart_goods_id_id_5f49ebce_fk_goods_id` (`goods_id_id`),
  KEY `userInfo_cart_order_id_id_9879c9b3_fk_orders_id` (`order_id_id`),
  CONSTRAINT `userInfo_cart_goods_id_id_5f49ebce_fk_goods_id` FOREIGN KEY (`goods_id_id`) REFERENCES `goods` (`id`),
  CONSTRAINT `userInfo_cart_order_id_id_9879c9b3_fk_orders_id` FOREIGN KEY (`order_id_id`) REFERENCES `orders` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cart
-- ----------------------------
INSERT INTO `cart` VALUES ('14', '1', '3', '29');
INSERT INTO `cart` VALUES ('15', '1', '10', '29');
INSERT INTO `cart` VALUES ('16', '2', '3', '30');
INSERT INTO `cart` VALUES ('17', '2', '3', '31');
INSERT INTO `cart` VALUES ('18', '2', '10', '31');
INSERT INTO `cart` VALUES ('19', '2', '11', '32');
INSERT INTO `cart` VALUES ('20', '3', '10', '33');
INSERT INTO `cart` VALUES ('21', '4', '11', '33');
INSERT INTO `cart` VALUES ('22', '1', '3', '34');
INSERT INTO `cart` VALUES ('23', '2', '10', '34');
INSERT INTO `cart` VALUES ('24', '2', '3', '35');
INSERT INTO `cart` VALUES ('25', '2', '3', '36');
INSERT INTO `cart` VALUES ('26', '2', '10', '37');
INSERT INTO `cart` VALUES ('27', '1', '10', '38');
INSERT INTO `cart` VALUES ('28', '1', '3', '39');
INSERT INTO `cart` VALUES ('29', '1', '3', '40');
INSERT INTO `cart` VALUES ('30', '2', '3', '41');
INSERT INTO `cart` VALUES ('31', '2', '3', '42');
INSERT INTO `cart` VALUES ('32', '1', '3', '43');
INSERT INTO `cart` VALUES ('33', '2', '3', '44');

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2019-01-25 04:06:59.906084', '1', '123', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2019-01-25 04:07:08.722045', '2', '123456', '1', '[{\"added\": {}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2019-01-25 04:07:27.491271', '1', '服装商品', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2019-01-25 04:07:35.207979', '2', '电子商品', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2019-01-25 04:07:53.531909', '3', '服装商品2', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2019-01-25 04:08:05.607480', '4', '电子商品2', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2019-01-25 04:08:31.469415', '1', '电脑', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2019-01-25 04:08:56.447649', '2', '羽绒服', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2019-01-25 04:09:17.387357', '1', '张三', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2019-01-25 04:09:29.765340', '2', '李四', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2019-01-25 04:09:41.602694', '3', '王五', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2019-01-25 04:09:56.180044', '1', '20190125120541170598', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2019-01-25 12:25:37.735993', '1', '20190125120541170598', '2', '[]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2019-01-25 12:26:13.586004', '2', '20190125122138769082', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2019-01-27 20:16:30.153879', '1', '20190125120541170598', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2019-01-28 16:07:09.004235', '4', '无名氏', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('17', '2019-01-28 16:07:16.176242', '5', '无名氏', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('18', '2019-01-28 16:07:25.099996', '6', '无名氏', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('19', '2019-01-28 16:07:33.083214', '7', '无名氏', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('20', '2019-01-28 16:07:40.083738', '8', '无名氏', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('21', '2019-01-30 11:16:13.460420', '3', '电脑', '2', '[{\"changed\": {\"fields\": [\"goods_kucun\", \"goods_jifen\"]}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('22', '2019-01-30 13:26:23.367485', '1', '张三', '2', '[{\"changed\": {\"fields\": [\"buy_people_keyongjifen\"]}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('23', '2019-01-31 19:52:34.969332', '26', '20190130131828287470', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('24', '2019-01-31 19:52:34.974504', '25', '20190130131828287470', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('25', '2019-01-31 19:52:34.979966', '24', '20190130131740854579', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('26', '2019-01-31 19:52:34.985614', '23', '20190130123722367672', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('27', '2019-01-31 19:52:35.026180', '22', '20190130123422643446', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('28', '2019-01-31 19:52:35.086981', '21', '20190130123422643446', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('29', '2019-01-31 19:52:35.096360', '20', '20190130123422643446', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('30', '2019-01-31 19:52:35.106441', '19', '20190130123422643446', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('31', '2019-01-31 19:52:35.115172', '18', '20190130123350154973', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('32', '2019-01-31 19:52:35.126178', '17', '20190130122923333679', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('33', '2019-01-31 19:52:35.135781', '16', '20190130121722815119', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('34', '2019-01-31 19:52:35.144488', '15', '20190129094422745737', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('35', '2019-01-31 19:52:35.153557', '13', '20190129092844609534', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('36', '2019-01-31 19:52:35.163760', '12', '20190128191142234080', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('37', '2019-01-31 19:52:35.174612', '11', '20190128184859736781', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('38', '2019-01-31 19:52:35.182832', '10', '20190128184803670937', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('39', '2019-01-31 19:52:35.191234', '9', '20190128174918556715', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('40', '2019-01-31 19:52:35.199384', '8', '20190128174735782825', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('41', '2019-01-31 19:52:35.208988', '7', '20190128172732358367', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('42', '2019-01-31 19:52:35.264164', '6', '20190128172732358367', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('43', '2019-01-31 19:52:35.274401', '5', '20190128172732358367', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('44', '2019-01-31 19:52:35.291469', '4', '20190128172732358367', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('45', '2019-01-31 19:52:35.300405', '3', '20190128172732358367', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('46', '2019-01-31 19:52:35.309572', '2', '20190125122138769082', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('47', '2019-01-31 19:52:35.318268', '1', '20190125120541170598', '3', '', '8', '1');
INSERT INTO `django_admin_log` VALUES ('48', '2019-02-25 10:08:04.714859', '2', 'python1', '1', '[{\"added\": {}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('49', '2019-02-25 10:09:03.618148', '2', 'python1', '2', '[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"email\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('50', '2019-02-25 10:12:30.250487', '2', 'python1', '2', '[{\"changed\": {\"fields\": [\"is_staff\"]}}]', '4', '1');

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('13', 'captcha', 'captchastore');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('10', 'userInfo', 'administrators');
INSERT INTO `django_content_type` VALUES ('11', 'userInfo', 'buy_peoples');
INSERT INTO `django_content_type` VALUES ('12', 'userInfo', 'cart');
INSERT INTO `django_content_type` VALUES ('9', 'userInfo', 'goods');
INSERT INTO `django_content_type` VALUES ('7', 'userInfo', 'goods_types');
INSERT INTO `django_content_type` VALUES ('8', 'userInfo', 'order');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-01-25 04:05:44.381966');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2019-01-25 04:05:45.168150');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2019-01-25 04:05:45.341403');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2019-01-25 04:05:45.380515');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2019-01-25 04:05:45.496703');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2019-01-25 04:05:45.594079');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2019-01-25 04:05:45.827104');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2019-01-25 04:05:45.878957');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2019-01-25 04:05:45.941378');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2019-01-25 04:05:45.946213');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2019-01-25 04:05:45.960238');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2019-01-25 04:05:46.096816');
INSERT INTO `django_migrations` VALUES ('13', 'sessions', '0001_initial', '2019-01-25 04:05:46.147776');
INSERT INTO `django_migrations` VALUES ('14', 'userInfo', '0001_initial', '2019-01-25 04:05:46.788526');
INSERT INTO `django_migrations` VALUES ('15', 'userInfo', '0002_auto_20190127_1948', '2019-01-27 19:48:37.992502');
INSERT INTO `django_migrations` VALUES ('16', 'userInfo', '0003_auto_20190127_1953', '2019-01-27 19:53:39.636859');
INSERT INTO `django_migrations` VALUES ('17', 'userInfo', '0004_auto_20190127_2056', '2019-01-27 20:56:09.805896');
INSERT INTO `django_migrations` VALUES ('18', 'userInfo', '0005_auto_20190127_2057', '2019-01-27 20:57:48.405633');
INSERT INTO `django_migrations` VALUES ('19', 'userInfo', '0006_auto_20190128_0918', '2019-01-28 09:18:30.829361');
INSERT INTO `django_migrations` VALUES ('20', 'userInfo', '0007_auto_20190128_1622', '2019-01-28 16:22:59.264508');
INSERT INTO `django_migrations` VALUES ('21', 'userInfo', '0008_auto_20190129_1227', '2019-01-29 12:27:35.452367');
INSERT INTO `django_migrations` VALUES ('22', 'userInfo', '0009_auto_20190130_1036', '2019-01-30 10:36:34.826571');
INSERT INTO `django_migrations` VALUES ('23', 'userInfo', '0010_auto_20190130_1141', '2019-01-30 11:41:03.426131');
INSERT INTO `django_migrations` VALUES ('24', 'captcha', '0001_initial', '2019-11-27 10:42:40.803451');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('9l6lqs8ovqhkv1r1strxoqscy28dus13', 'YWVlN2YwM2JkYzgwZTM5ZGI4OTE1NThmZTFkMjY0YTVmMTk3YjhjYjp7fQ==', '2019-11-08 17:03:57.815962');
INSERT INTO `django_session` VALUES ('mp6rezq0b8dtpjtljhbho2b7p0poa71w', 'MTE5ZmFhMjIyODdiNDA5OGRmNmE2NGZjZTM1YWM0ZmUyZjFlMmNkODp7ImFkbWluaXN0cmF0b3JfaWQiOiIxMjMiLCJ1aWQiOjF9', '2019-12-16 14:59:33.674047');
INSERT INTO `django_session` VALUES ('mxf9qcla8rjl76t2ain4cj4byz8pxg2c', 'YWVlN2YwM2JkYzgwZTM5ZGI4OTE1NThmZTFkMjY0YTVmMTk3YjhjYjp7fQ==', '2019-07-29 10:05:27.633284');
INSERT INTO `django_session` VALUES ('q4t8zn4u8p5a2uh6cbxyxcxhh7txmgt8', 'MTE5ZmFhMjIyODdiNDA5OGRmNmE2NGZjZTM1YWM0ZmUyZjFlMmNkODp7ImFkbWluaXN0cmF0b3JfaWQiOiIxMjMiLCJ1aWQiOjF9', '2019-11-19 13:25:47.397772');
INSERT INTO `django_session` VALUES ('qnvqwrnccr64apti2avv9hjvstu6yaev', 'NzRlZGJlYWExZTc2YzU2NmVkYzk5ZDZjNGRhNzQ0MjRmMTFhMGU1ODp7InVpZCI6MSwiYWRtaW5pc3RyYXRvcl9pZCI6IjEyMyJ9', '2019-07-29 10:10:47.021901');
INSERT INTO `django_session` VALUES ('v61i4e39c065sclrkgqeso83h488ts50', 'MTE5ZmFhMjIyODdiNDA5OGRmNmE2NGZjZTM1YWM0ZmUyZjFlMmNkODp7ImFkbWluaXN0cmF0b3JfaWQiOiIxMjMiLCJ1aWQiOjF9', '2019-09-02 10:46:54.053014');
INSERT INTO `django_session` VALUES ('ywubo3lgoreye5p54bjifmm2laee574s', 'YWVlN2YwM2JkYzgwZTM5ZGI4OTE1NThmZTFkMjY0YTVmMTk3YjhjYjp7fQ==', '2020-01-16 15:33:13.810940');
INSERT INTO `django_session` VALUES ('zrxz0fleskj5h57wnnb4yhj5auxl3amr', 'MTE5ZmFhMjIyODdiNDA5OGRmNmE2NGZjZTM1YWM0ZmUyZjFlMmNkODp7ImFkbWluaXN0cmF0b3JfaWQiOiIxMjMiLCJ1aWQiOjF9', '2019-08-23 14:01:59.024284');

-- ----------------------------
-- Table structure for `goods`
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_id` varchar(50) NOT NULL,
  `goods_name` varchar(50) NOT NULL,
  `goods_price` decimal(10,2) NOT NULL,
  `goods_kucun` int(11) NOT NULL,
  `goods_xiaoliang` int(11) NOT NULL,
  `goods_text` longtext NOT NULL,
  `goods_guige` varchar(100) NOT NULL,
  `administrator_id_id` int(11) NOT NULL,
  `goods_type_id` int(11) NOT NULL,
  `goods_jifen` decimal(7,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_administrator_id_id_f4ef6b68_fk_super_user_id` (`administrator_id_id`),
  KEY `goods_goods_type_id_57643bb9_fk_goods_types_id` (`goods_type_id`),
  CONSTRAINT `goods_administrator_id_id_f4ef6b68_fk_super_user_id` FOREIGN KEY (`administrator_id_id`) REFERENCES `super_user` (`id`),
  CONSTRAINT `goods_goods_type_id_57643bb9_fk_goods_types_id` FOREIGN KEY (`goods_type_id`) REFERENCES `goods_types` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO `goods` VALUES ('3', 'ID0001', '电脑', '123.50', '971', '19', '暂无描述', '无', '1', '2', '100.11');
INSERT INTO `goods` VALUES ('4', '123', '无名氏', '123.00', '0', '0', '暂无描述', '无', '1', '2', '100.00');
INSERT INTO `goods` VALUES ('5', '1234', '无名氏', '123.00', '0', '0', '暂无描述', '无', '1', '2', '100.00');
INSERT INTO `goods` VALUES ('6', '123455', '无名氏', '0.05', '0', '0', '暂无描述', '无', '1', '1', '100.00');
INSERT INTO `goods` VALUES ('8', '1232131', '无名氏', '1231.00', '0', '0', '暂无描述', '无', '1', '1', '100.00');
INSERT INTO `goods` VALUES ('9', 'ID0002', '羽绒服', '1232.00', '81', '4', '暂无描述', '无', '1', '2', '100.00');
INSERT INTO `goods` VALUES ('10', '123121', '无名氏', '12312.00', '153', '19', '暂无描述', '无', '1', '2', '100.00');
INSERT INTO `goods` VALUES ('11', '123231133', 'haha', '100.00', '6', '6', '暂无描述', '无', '1', '1', '122.11');
INSERT INTO `goods` VALUES ('13', 'ID0099', 'Nike', '124.12', '3', '0', '暂无描述', '无', '1', '2', '0.01');

-- ----------------------------
-- Table structure for `goods_types`
-- ----------------------------
DROP TABLE IF EXISTS `goods_types`;
CREATE TABLE `goods_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `leibie_id` varchar(20) NOT NULL,
  `leixing` varchar(50) NOT NULL,
  `jibie` varchar(15) NOT NULL,
  `administrator_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_types_administrator_id_id_57525f64_fk_super_user_id` (`administrator_id_id`),
  CONSTRAINT `goods_types_administrator_id_id_57525f64_fk_super_user_id` FOREIGN KEY (`administrator_id_id`) REFERENCES `super_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_types
-- ----------------------------
INSERT INTO `goods_types` VALUES ('1', 'LB0001', '服装商品', '一级', '1');
INSERT INTO `goods_types` VALUES ('2', 'LB0002', '电子商品', '一级', '1');
INSERT INTO `goods_types` VALUES ('3', 'LB0001', '服装商品2', '一级', '2');
INSERT INTO `goods_types` VALUES ('4', 'LB0002', '电子商品2', '一级', '2');

-- ----------------------------
-- Table structure for `orders`
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` varchar(50) NOT NULL,
  `dingdanshijian` datetime(6) NOT NULL,
  `chengjiao_allmoney` decimal(7,2) NOT NULL,
  `youhuijine` decimal(7,2) NOT NULL,
  `goumailiang` int(11) NOT NULL,
  `huodejifen` decimal(7,2) NOT NULL,
  `zhifufangshi` varchar(20) NOT NULL,
  `order_is_show` tinyint(1) NOT NULL,
  `administrator_id_id` int(11) NOT NULL,
  `buy_prople_id` int(11) NOT NULL,
  `chengjiao_money` decimal(7,2) NOT NULL,
  `xiaohaojifen` decimal(7,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_administrator_id_id_1c0fb3ec_fk_super_user_id` (`administrator_id_id`),
  KEY `orders_buy_prople_id_c20e8aa7_fk_buy_peoples_id` (`buy_prople_id`),
  CONSTRAINT `orders_administrator_id_id_1c0fb3ec_fk_super_user_id` FOREIGN KEY (`administrator_id_id`) REFERENCES `super_user` (`id`),
  CONSTRAINT `orders_buy_prople_id_c20e8aa7_fk_buy_peoples_id` FOREIGN KEY (`buy_prople_id`) REFERENCES `buy_peoples` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO `orders` VALUES ('27', '20190130131926144196', '2019-01-30 13:19:47.470655', '0.00', '0.00', '2', '0.00', 'e', '0', '1', '2', '0.00', '200.00');
INSERT INTO `orders` VALUES ('28', '20190130132022813813', '2019-01-30 13:21:05.025489', '0.00', '0.00', '3', '0.00', 'e', '0', '1', '2', '0.00', '300.00');
INSERT INTO `orders` VALUES ('29', '20190130132413275928', '2019-01-30 13:24:31.468832', '0.00', '0.00', '2', '0.00', 'e', '0', '1', '2', '0.00', '200.11');
INSERT INTO `orders` VALUES ('30', '20190130132413275928', '2019-01-30 13:26:37.789631', '0.00', '0.00', '2', '0.00', 'e', '0', '1', '1', '0.00', '200.22');
INSERT INTO `orders` VALUES ('31', '20190130132413275928', '2019-01-30 13:27:01.796978', '0.00', '0.00', '4', '0.00', 'e', '0', '1', '1', '0.00', '400.22');
INSERT INTO `orders` VALUES ('32', '20190201193829731888', '2019-02-01 19:39:02.410384', '200.00', '0.00', '2', '2.00', 'd', '0', '1', '2', '200.00', '0.00');
INSERT INTO `orders` VALUES ('33', '20190201193829731888', '2019-02-01 19:39:44.747007', '37336.00', '0.00', '7', '373.36', 'b', '0', '1', '2', '37336.00', '0.00');
INSERT INTO `orders` VALUES ('34', '20190201193829731888', '2019-02-01 19:40:15.944188', '24747.50', '0.00', '3', '247.47', 'a', '0', '1', '2', '24747.50', '0.00');
INSERT INTO `orders` VALUES ('35', '20190201194319929243', '2019-02-01 19:43:34.281563', '247.00', '0.00', '2', '2.47', 'a', '1', '1', '1', '247.00', '0.00');
INSERT INTO `orders` VALUES ('36', '20190201194319929243', '2019-02-01 19:43:47.118303', '247.00', '0.00', '2', '2.47', 'b', '1', '1', '1', '247.00', '0.00');
INSERT INTO `orders` VALUES ('37', '20190201194319929243', '2019-02-01 19:44:31.240655', '24624.00', '0.00', '2', '246.24', 'a', '1', '1', '1', '24624.00', '0.00');
INSERT INTO `orders` VALUES ('38', '20190204151529562556', '2019-02-04 15:16:28.760437', '12312.00', '0.00', '1', '123.12', 'c', '1', '1', '1', '12312.00', '0.00');
INSERT INTO `orders` VALUES ('39', '20190204151529562556', '2019-02-04 15:17:19.920473', '123.50', '0.00', '1', '1.23', 'a', '1', '1', '1', '123.50', '0.00');
INSERT INTO `orders` VALUES ('40', '20190205140940870645', '2019-02-05 14:09:40.871313', '123.50', '0.00', '1', '1.23', 'a', '1', '1', '1', '123.50', '0.00');
INSERT INTO `orders` VALUES ('41', '20190205140956353332', '2019-02-05 14:09:56.353962', '247.00', '0.00', '2', '2.47', 'a', '1', '1', '1', '247.00', '0.00');
INSERT INTO `orders` VALUES ('42', '20190205144124448171', '2019-02-05 14:41:24.449182', '247.00', '0.00', '2', '2.47', 'a', '1', '1', '2', '247.00', '0.00');
INSERT INTO `orders` VALUES ('43', '20190212154654209640', '2019-02-12 15:46:54.212075', '123.50', '0.00', '1', '12.30', 'a', '1', '1', '1', '123.50', '0.00');
INSERT INTO `orders` VALUES ('44', '20190212154735132774', '2019-02-12 15:47:35.133504', '247.00', '0.00', '2', '24.70', 'a', '1', '1', '2', '247.00', '0.00');

-- ----------------------------
-- Table structure for `super_user`
-- ----------------------------
DROP TABLE IF EXISTS `super_user`;
CREATE TABLE `super_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `administrator_id` int(11) NOT NULL,
  `administrator_name` varchar(30) NOT NULL,
  `administrator_pwd` varchar(100) NOT NULL,
  `administrator_jifen` decimal(4,2) NOT NULL,
  `administrator_email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of super_user
-- ----------------------------
INSERT INTO `super_user` VALUES ('1', '123', '店小二', '40bd001563085fc35165329ea1ff5c5ecbdbbeef', '0.10', '18733181565@163.com');
INSERT INTO `super_user` VALUES ('2', '123456', 'root2', '7c4a8d09ca3762af61e59520943dc26494f8941b', '1.00', '1234545@163.com');
INSERT INTO `super_user` VALUES ('3', '12355798', '啊啊啊啊啊啊', 'f4542db9ba30f7958ae42c113dd87ad21fb2eddb', '1.00', '123@163.com');
INSERT INTO `super_user` VALUES ('4', '0', '000', '7c4a8d09ca3762af61e59520943dc26494f8941b', '1.00', '123@163.com');
