import 'package:flutter/material.dart';

//packages for scraping
import 'dart:io';
import 'package:http/http.dart' as http; // Contains a client for making API calls
import 'package:html/parser.dart'; // Contains HTML parsers to generate a Document object

class Login extends StatefulWidget{
  @override
  LoginState createState() => new LoginState();
}

class LoginState extends State<Login> {
  String url = "https://ps2.millburn.org";
  String username;
  String pass;
  String actType;
  var urlText  = TextEditingController();
  var userText = TextEditingController();
  var passText = TextEditingController();

  @override
  void initState(){
    super.initState();
  }

  Future initiate() async {
    debugPrint(username);
    debugPrint(pass);
    debugPrint(actType);
    debugPrint(url);

    var client = http.Client();
    http.Response response = await client.get(url);

    var document = parse(response.body);

    var userInput = document.querySelector("#fieldAccount");
    var passInput = document.querySelector("#fieldPassword");

    var PSTOKEN = document.querySelector("pstoken");
//    var PSTOKEN = document.querySelector("#pstoken").appendHtml('<div lc="any-value" >xxx</div>', treeSanitizer: new NullTreeSanitizer());
    var CONTEXTDATA = document.querySelector("#contextData");
    //FOR CUSTOM ATTRIBUTES
    //document.querySelector('body').appendHtml('<div lc="any-value" >xxx</div>', treeSanitizer: new NullTreeSanitizer());

    debugPrint(userInput.toString());
    debugPrint(passInput.toString());
    debugPrint(PSTOKEN.toString());
    debugPrint(CONTEXTDATA.toString());

/*
    var b = {
      'pstoken': PSTOKEN,
      'contextData': CONTEXTDATA,
      'dbpw': '',
      'translator_username': '',
      'translator_password': '',
      'translator_ldappassword': '',
      'returnUrl': url,
      'serviceName': 'PS Parent Portal',
      'serviceTicket': '',
      'pcasServerUrl': '',
      'credentialType': 'User Id and Password Credential',
      'account': username,
      'pw': pass,
      'translatorpw': ''
    };
    http.post(url, body: b);

    http.post(url, body: b)
        .then((response) {
      debugPrint("Response status: ${response.statusCode}");
      debugPrint("Response body: ${response.body}");
    });
*/
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Theme.of(context).backgroundColor,
      body: Stack(
        children: <Widget>[
//          title
          Container (
            alignment: Alignment(0.0, -0.5),
            color: Theme.of(context).primaryColor,
            height: 150,
            child: Center (
              child: Text(
                'PowerGPA',
                style: new TextStyle(
                  color: Theme.of(context).secondaryHeaderColor,
                  fontSize: 48.0)
                ),
//                textAlign: TextAlign.center,
              )
            ),

//          textfields
          Container(
            alignment: Alignment(0, 1),
//          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                TextFormField(
                  controller: urlText,
                  decoration: new InputDecoration(labelText: "PowerSchool Url: ", hintText: "https://ps2.millburn.org"),
                ),
                TextField(
                  controller: userText,
                  decoration: new InputDecoration(labelText: "PowerSchool Username: "),
                ),
                TextField(
                  controller: passText,
                  decoration: new InputDecoration(labelText: "PowerSchool Password: "),
                  obscureText: true,
                ),
                DropdownButton<String>(
                  hint: Text("Account Type"),
                  items: <String>['Student', 'Parent'].map((String value) {
                    return new DropdownMenuItem<String>(
                      value: value,
                      child: new Text(value),
                    );
                  }).toList(),
                  onChanged: (String newVal) {
                    actType = newVal;
                    debugPrint(newVal);
                  },
                ),
                MaterialButton(
                  color: Theme.of(context).primaryColor,
                  textColor: Theme.of(context).secondaryHeaderColor,
                  highlightColor: Theme.of(context).highlightColor,
                  child: Text(
                    "Login",
                    style: TextStyle(
                    fontSize: 25
                    ),
                  ),
                  onPressed: (){
                    username = userText.text; pass = passText.text;
                    if(username != "" && pass != "" && actType != ""){
                      if(urlText.text != ""){
                        //CHECK IF URL IS HTTPS
                        if(urlText.text.startsWith('https://')) {
                          url = urlText.text;
                        }
                        else{
                          url = "https://" + urlText.text;
                        }
                      }
                      initiate();
                      //LOAD NEW PAGE
                    }
                  },
                )
              ],
            ),
          ),
        ],
      ),
    );
  }//build

}//class