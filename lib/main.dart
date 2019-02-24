import 'package:flutter/material.dart';
import 'login.dart';
import 'package:flutter/services.dart';
//import 'dashboard.dart';

void main(){
  SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp])
      .then((_) {
    runApp(App());
  });
}

class App extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
      title: 'NexGenMath',
      debugShowCheckedModeBanner: false,
      theme: new ThemeData(
        backgroundColor: Color(0xFFffffff),
        accentColor: Color(0xFF9c27b0),
        primaryColor: Color(0xFF2196f3),
//      border color
        primaryColorDark: Color(0xFFdddddd),
//      font color
        textSelectionColor: Color(0xFF666666),
        highlightColor: Color(0xFF0d8aee),
        secondaryHeaderColor: Color(0xFFFFFFFF),
        fontFamily: 'Roboto'
      ),

      initialRoute: '/',
      routes: {
        '/': (_) => new Login(),
//        '/dashboard': (_) => new Dashboard(),
      },
    );
  }
}