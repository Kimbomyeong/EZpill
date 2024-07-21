import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:ezpill/Screens/pill_detail_screen.dart';
import 'package:ezpill/widgets/app_bar_widget.dart';

class ProfileScreen extends StatefulWidget {
  const ProfileScreen({Key? key}) : super(key: key);

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  List<String> likedPills = [];

  var _isChecked = false;

  @override
  void initState() {
    super.initState();
    initLikedPills();
  }

  void initLikedPills() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    List<String>? storedLikedPills = prefs.getStringList('likedPills');
    setState(() {
      likedPills = storedLikedPills ?? [];
    });
  }

  Future<Map<String, dynamic>> getProductInfo(String productId) async {
    final apiUrl = Uri.parse(
        'http://ec2-13-209-244-84.ap-northeast-2.compute.amazonaws.com/ezpill/get-product-info/$productId/');

    var response = await http.get(apiUrl);
    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load product info');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: const PreferredSize(
        preferredSize: Size.fromHeight(60),
        child: AppBarWidget(
          screentitle: "내 정보",
        ),
      ),
      body: Container(
        padding: const EdgeInsets.fromLTRB(30, 90, 30, 60),
        child: Column(
          children: [
            const Align(
              alignment: Alignment.topLeft,
              child: Text(
                '____님\n오늘도 건강하세요!',
                style: TextStyle(
                  fontFamily: "NanumSquare",
                  fontSize: 30,
                  fontWeight: FontWeight.w700,
                ),
              ),
            ),
            const SizedBox(
              height: 20,
            ),
            Container(
              height: 160,
              decoration: ShapeDecoration(
                color: Colors.white,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(30),
                ),
                shadows: const [
                  BoxShadow(
                    color: Color(0x3F000000),
                    blurRadius: 4,
                    offset: Offset(0, 4),
                    spreadRadius: 1,
                  )
                ],
              ),
              child: Column(
                children: [
                  const SizedBox(
                    height: 20,
                  ),
                  const Row(
                    mainAxisAlignment: MainAxisAlignment.start,
                    children: [
                      SizedBox(
                        width: 20,
                      ),
                      Text(
                        '내 영양제',
                        style: TextStyle(
                          color: Colors.black,
                          fontSize: 25,
                          fontFamily: 'NanumSquare',
                          fontWeight: FontWeight.w700,
                          height: 0,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(
                    height: 10,
                  ),
                  SizedBox(
                    width: 300,
                    height: 80,
                    child: Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 12),
                      child: ListView.separated(
                        scrollDirection: Axis.horizontal,
                        itemCount: likedPills.length,
                        separatorBuilder: (context, index) =>
                            const SizedBox(width: 12),
                        itemBuilder: (context, index) {
                          return GestureDetector(
                            child: Container(
                              width: 80,
                              height: 80,
                              decoration: const BoxDecoration(
                                boxShadow: [
                                  BoxShadow(
                                    color: Color(0x3F000000),
                                    blurRadius: 5,
                                    offset: Offset(0, 4),
                                    spreadRadius: 0,
                                  ),
                                ],
                              ),
                              child: Image.asset(
                                  'assets/images/${likedPills[index]}.jpg'),
                            ),
                            onTap: () {
                              getProductInfo(likedPills[index])
                                  .then((productInfo) {
                                Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                    builder: (context) => PillDetailScreen(
                                      productInfo: productInfo,
                                      product_id: likedPills[index],
                                      updateLikedPills:
                                          (List<String> likedPills) {
                                        setState(() {
                                          this.likedPills = likedPills;
                                        });
                                      },
                                    ),
                                  ),
                                );
                              }).catchError((error) {
                                print(error);
                                // Handle error (e.g., show an error message)
                              });
                            },
                          );
                        },
                      ),
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(
              height: 40,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                const Text(
                  '알림 설정',
                  style: TextStyle(
                    color: Colors.black,
                    fontSize: 30,
                    fontFamily: 'NanumSquare',
                    fontWeight: FontWeight.w700,
                    height: 0,
                  ),
                  textAlign: TextAlign.start,
                ),
                Switch(
                  value: _isChecked,
                  onChanged: (value) {
                    setState(() {
                      _isChecked = value;
                    });
                  },
                ),
              ],
            ),
            const SizedBox(
              height: 20,
            ),
            const Align(
              alignment: Alignment.centerLeft,
              child: Text(
                '이용약관',
                style: TextStyle(
                  color: Colors.black,
                  fontSize: 30,
                  fontFamily: 'NanumSquare',
                  fontWeight: FontWeight.w700,
                  height: 0,
                ),
                textAlign: TextAlign.start,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
