import 'package:ezpill/widgets/app_bar_widget.dart';
import 'package:flutter/material.dart';
import 'package:table_calendar/table_calendar.dart';

class CalendarScreen extends StatelessWidget {
  const CalendarScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const PreferredSize(
        preferredSize: Size.fromHeight(60),
        child: AppBarWidget(screentitle: "달력"),
      ),
      body: TableCalendar(
        locale: 'ko_KR',
        firstDay: DateTime.utc(2023, 1, 1),
        lastDay: DateTime.utc(2033, 12, 31),
        focusedDay: DateTime.now(),
        daysOfWeekHeight: 30,
        headerStyle: const HeaderStyle(
          formatButtonVisible: false,
          titleCentered: true,
        ),
        calendarStyle: CalendarStyle(
          todayDecoration: BoxDecoration(
            borderRadius: BorderRadius.circular(10),
            color: const Color(0xFFF9B53A),
          ),
          todayTextStyle: const TextStyle(
            color: Colors.white,
            fontSize: 25,
            fontFamily: 'Gmarket Sans TTF',
            fontWeight: FontWeight.w500,
            height: 0,
          ),
          weekendTextStyle: const TextStyle(
            color: Colors.black,
            fontSize: 25,
            fontFamily: 'Gmarket Sans TTF',
            fontWeight: FontWeight.w500,
            height: 0,
          ),
          defaultTextStyle: const TextStyle(
            color: Colors.black,
            fontSize: 25,
            fontFamily: 'Gmarket Sans TTF',
            fontWeight: FontWeight.w500,
            height: 0,
          ),
        ),
      ),
    );
  }
}
