/////////////////////////////EXPO EXAMPLE BASE////////////////////////////////////
// https://levelup.gitconnected.com/how-to-click-images-in-react-native-using-expo-camera-for-android-1fbc1181473d
// base tutorial from here: https://medium.com/@nutanbhogendrasharma/implement-camera-in-react-native-mobile-app-part-1-ea307ce924a4
// https://www.freecodecamp.org/news/how-to-create-a-camera-app-with-expo-and-react-native/

//////////////////////////////////Test Code/////////////////////////////////////////
// Navigate between screens: https://reactnavigation.org/docs/navigating
// In App.js in a new project

import * as React from 'react';
import { View, Text, ScrollView, Image, Dimensions } from 'react-native';
import { NavigationContainer, useFocusEffect } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { Button, Switch, Alert, StyleSheet, TouchableOpacity } from 'react-native';
import { SelectList } from 'react-native-dropdown-select-list';
import { useState, useEffect } from 'react';
import { CameraType } from 'expo-camera';
import { Camera } from 'expo-camera';
import { storage } from "./firebase_setup.js";
import { uploadBytesResumable, ref, getDownloadURL, listAll } from 'firebase/storage';
import AsyncStorage from '@react-native-async-storage/async-storage';


///////////////////// Styling //////////////////
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: '#01A39E'
  },
  camera: {
    flex: 1,
  },
  button: {
    alignSelf: 'flex-end',
    alignItems: 'center',
    justifyContent: 'center',
    color: '#FFFFFF'
  },
  buttonContainer: {
    flexDirection: 'row',
    backgroundColor: 'transparent',
    alignItems: 'center',
    justifyContent: 'space-evenly',

  },
  homeButtonContainer: {
    flexDirection: 'column',
    backgroundColor: '#87e0de',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: 10,
    borderRadius: 10,
    margin: 10
  },
  cameraButtonContainer: {
    flex: .9,
    flexDirection: 'row',
    backgroundColor: 'transparent',
    alignItems: 'center',
    justifyContent: 'space-evenly',
  },
  homeButtonText: {
    fontSize: 36,
    color: "#fff",
    fontWeight: "bold",
    alignSelf: "center",
    textTransform: "uppercase"
  },
  settingsButtonText: {
    fontSize: 24,
    color: "#fff",
    fontWeight: "bold",
    alignSelf: "center",
    textTransform: "uppercase"
  },
  text: {
    fontSize: 24,
    fontWeight: 'bold',
    color: 'white',
    alignItems: 'center'
  },
  genericContainer: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: "#01A39E",
  },
  image: {
    width: 700,
    height: 700,
    resizeMode: 'contain',
    marginBottom: 20,
  },
  line: {
    borderBottomWidth: 1,
    borderBottomColor: 'black',
    width: '100%',
    marginBottom: 50,
  }
});

// generic getData
const getData = async (key) => {
  try {
    value = await AsyncStorage.getItem(key);
    if (value !== null) {
      // value previously stored
    }
  } catch (e) {
    // error reading value
  }
}

// generic storeData
const storeData = async (key, value) => {
  try {
    await AsyncStorage.setItem(key, value);
    console.log("Stored");
  } catch (e) {
    // saving error
  }
}

/////////////////// Home Screen ////////////////////////
// get data between screens: https://www.geeksforgeeks.org/how-to-pass-value-between-screens-in-react-native/
function HomeScreen({ navigation, route }) {
  // retrieve settings data
  const [outerValue, setOuterValue] = useState(null);
  const [oldID, setOldID] = useState();
  // specialized getData for setting settings on front end
  const getData = async () => {
    try {
      value = await AsyncStorage.getItem('@stringSettingsObj');

      if (value !== null) {
        // value previously stored
        setOuterValue(value);
      }
    } catch (e) {
      // error reading value
      console.log("Home screen error: ", e);
    }
  }
  const getOldID = async () => {
    try {
      value = await AsyncStorage.getItem('@photoIntervalID');

      if (value !== null) {
        // value previously stored
        setOldID(value);
      }
    } catch (e) {
      // error reading value
      console.log("Home screen error: ", e);
    }
  }
  useFocusEffect(() => {
    getData();
    getOldID();
  });
  // Clear old interval
  clearInterval(parseInt(oldID));

  return (
    <View style={styles.genericContainer}>
      <View style={styles.homeButtonContainer}>
        <TouchableOpacity onPress={() => navigation.navigate('RobotControls')}>
          <Text style={styles.homeButtonText}>{"Settings"}</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.homeButtonContainer}>
        <TouchableOpacity onPress={() => {
          navigation.navigate('CameraScreen', {});
        }}>
          <Text style={styles.homeButtonText}>{"Camera"}</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.homeButtonContainer}>
        <TouchableOpacity onPress={() => navigation.navigate('PhotoScreen')}>
          <Text style={styles.homeButtonText}>{"Photo Viewer"}</Text>
        </TouchableOpacity>


      </View>

    </View>
  );
}
////////////////// Robot Controls /////////////////////////////




function sendMsg(input) {
  try {
    console.log(input);
    ws.send(input);
  } catch {
    console.log("Message could not be sent");
  }

};
let connectionFlag = 0;
function RobotControls({ navigation }) {
  /////////////// status check ///////////////
  const [status, setStatus] = useState({ text: 'Loading...', color: 'orange' });
  const [retry, setRetryButton] = useState(true);

  function checkConnection() {
    if (ws.readyState === ws.OPEN && connectionFlag !== 1) {
      console.log('Connection is open');
      connectionFlag = 1;
      setStatus({ text: 'Robot Status: Connected', color: 'green' });
      setRetryButton(false);
    } else if (ws.readyState !== ws.OPEN && connectionFlag !== 2) {
      console.log('Connection is closed');
      connectionFlag = 2;
      setStatus({ text: 'Robot Status: Disconnected', color: 'red' });
      setRetryButton(true)
    }
  }
  setInterval(checkConnection, 2000);

  // init settings values
  const [selected, setSelected] = React.useState("");
  const [isEnabled, setIsEnabled] = useState(false);
  // get existing cache values, use to show current settings

  async function getSettings() {
    try {
      const settings = await AsyncStorage.getItem('@stringSettingsObj') // get existing data, use that for settings on initial load
      var parsedSettings = JSON.parse(settings);
      setSelected(parseInt(parsedSettings.selectedKey));
      setIsEnabled(parsedSettings.isEnabledKey);
      //console.log("Parsed settings: ", parsedSettings);
    } catch (error) {
      console.log("get settings error on settings page: ", error);
    }
  }
  useState(() => {
    getSettings();
  });

  //////////// camera delay selection code //////////////
  delay = 10;
  const data = [
    { key: '1', value: '10 Seconds' },
    { key: '2', value: '15 Seconds' },
    { key: '3', value: '30 Seconds' },
  ]
  if (selected == undefined) {
    setSelected(10); // default delay
  }
  if (isEnabled == undefined) { // default auto photo
    setIsEnabled(false);
  }
  delay = parseInt(selected); // int version of selected from dropdown menu

  /////////////// auto capture code ///////////////

  const toggleSwitch = () => {
    setIsEnabled(previousState => !previousState);
  };

  // settings object
  let settingsObj = {
    selectedKey: selected,
    isEnabledKey: isEnabled
  }

  return (
    <View style={styles.genericContainer}>
      <Text style={{ color: status.color }}>{status.text}</Text>
      {retry && (
        <Button title="Reconnect" onPress={() => serverConnection()} />

      )}
      <View style={styles.homeButtonContainer}>
        <TouchableOpacity onPress={() => sendMsg('start')}>
          <Text style={styles.settingsButtonText}>{"Start Robot"}</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.homeButtonContainer}>
        <TouchableOpacity onPress={() => sendMsg('stop')}>
          <Text style={styles.settingsButtonText}>{"Stop Robot"}</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.homeButtonContainer}>
        <View style={styles.buttonContainer}>
          <Text style={styles.settingsButtonText}>{"Autocapture Enable"}</Text>
          <Switch
            trackColor={{ false: '#63fa05', true: '#54f542' }}
            thumbColor={isEnabled ? '#fff' : '#545353'}
            onValueChange={toggleSwitch}
            value={isEnabled}>
          </Switch>
        </View>
      </View>
      <View style={styles.homeButtonContainer}>
        <Text style={styles.settingsButtonText}>{"Autocapture Delay"}
        </Text>
        <SelectList
          boxStyles={{ backgroundColor: "#87e0de", borderRadius: 0, }}
          dropdownStyles={{ backgroundColor: "#87e0de" }}
          search={false}
          setSelected={(selected) => setSelected(selected)}
          data={data}
          save="value"
          color="#fff"
        >
        </SelectList>
      </View>
      <View style={styles.homeButtonContainer}>
        <TouchableOpacity onPress={async () => {
          var stringSettingsObj = JSON.stringify(settingsObj);
          await storeData('@stringSettingsObj', JSON.stringify(settingsObj));
          navigation.navigate('Home')
        }}>
          <Text style={styles.settingsButtonText}>{"Apply Changes"}</Text>
        </TouchableOpacity>
      </View>
    </View >
  );
};

///////////////// Camera Screen /////////////////////////
function CameraScreen({ navigation }) {
  const [type, setType] = useState(CameraType.back);
  const [permission, requestPermission] = Camera.useCameraPermissions();
  const [cameraRef, setCameraRef] = useState(null);

  // hooks have to be above return statements
  const [delay, setDelay] = useState();
  const [enabled, setEnabled] = useState();
  const [oldID, setOldID] = useState();

  async function getSettings() {
    try {
      const settings = await AsyncStorage.getItem('@stringSettingsObj') // get existing data, use that for settings on initial load
      var parsedSettings = JSON.parse(settings);
      setDelay(parseInt(parsedSettings.selectedKey));
      setEnabled(parsedSettings.isEnabledKey);
      //console.log("Parsed settings: ", parsedSettings);
    } catch (error) {
      console.log("get settings error: ", error);
    }

  }
  async function getID() {
    try {
      const ID = await AsyncStorage.getItem('@photoIntervalID');
      if (ID == undefined) {
        ID = 0;
      }
      //console.log("old ID: ", ID);
      setOldID(parseInt(ID));
    } catch (error) {
      console.log("get ID error: ", error);

    }
  }

  getSettings();
  getID();

  // Clear old interval
  useEffect(() => {
    clearInterval(parseInt(oldID));
  })


  if (!permission) {
    // Camera permissions are still loading
    return <View />;
  }

  if (!permission.granted) {
    // Camera permissions are not granted yet
    return (
      <View style={styles.container}>
        <Text style={{ textAlign: 'center' }}>We need your permission to show the camera</Text>
        <Button onPress={requestPermission} title="grant permission" />
      </View>
    );
  }

  function toggleCameraType() {
    setType(current => (current === CameraType.back ? CameraType.front : CameraType.back));
  }

  return (
    <View style={styles.container}>
      <Camera style={styles.camera} type={type} ref={(ref) => { setCameraRef(ref); }}>
        <View style={styles.cameraButtonContainer}>
          <TouchableOpacity style={styles.button} onPress={toggleCameraType}>
            <Text style={styles.text}>Flip Camera</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={async () => {
            async function autoPhotoCapture() {
              var photo = await cameraRef.takePictureAsync();
              uploadImage(photo.uri); // comment out for testing
              console.log("Auto capture URI: ", photo.uri);
            }

            if (!enabled) {
              try {
                clearInterval(parseInt(oldID));
                console.log("Interval cleared");
              } catch (error) {
                console.log("clear interval error: ", error);
              }
            } else {
              try {
                //console.log("old id: ", oldID);
                clearInterval(parseInt(oldID)); // oldID not clearing
                var photoIntervalID = setInterval(autoPhotoCapture, delay * 1000);
                // use clearInterval(photoInvervalID) to stop interval
                if (photoIntervalID) {
                  //console.log("store id: ", photoIntervalID);
                  storeData('@photoIntervalID', String(photoIntervalID));
                }
                // console.log("Current ID: ", photoIntervalID);
                // console.log("Old interval cleared");
              } catch (error) {
                console.log("Enabled error");
                throw error;
              }

            }
            if (cameraRef && !enabled) {
              try {
                var photo = await cameraRef.takePictureAsync();
                const uri = photo.uri
                console.log(photo.uri);
                uploadImage(uri); // comment out for testing
              } catch (error) {
                console.log("take pic error: ", error);
              }


            }
          }}>
            <Text style={styles.text}>Take Photo</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('RobotControls')}>
            <Text style={styles.text}>Settings</Text>
          </TouchableOpacity>
        </View>
      </Camera >
    </View >
  );
};

/////////////////Cloud Upload////////////////////

const uploadImage = async (uri) => {
  const filename = uri.substring(uri.lastIndexOf('/') + 1);
  const uploadUri = uri.replace('file://', '');

  // Fetch the file contents and convert to a Blob
  const response = await fetch(uploadUri);
  const blob = await response.blob();

  const timestamp = Date.now();
  const imageName = `my-image-${timestamp}.jpg`;
  const storageRef = ref(storage, imageName);
  const uploadTask = uploadBytesResumable(storageRef, blob);

  console.log("Photo Upload to firebase");
};

////////////////Cloud List all Images/////////////////
//https://firebase.google.com/docs/storage/web/list-files
//https://stackoverflow.com/questions/37335102/how-to-get-a-list-of-all-files-in-cloud-storage-in-a-firebase-app

const ListImagesInBucket = async () => {
  // Create a reference under which you want to list
  const imageDir = ''; //hardcoded for now
  const listRef = ref(storage, imageDir);
  const results = await listAll(listRef);
  const item_list = await Promise.all(results.items.map((itemRef) => getDownloadURL(itemRef)));
  return item_list;
}

//////////////Photo display screen ////////////////////
function PhotoScreen() {
  const [imageList, setImageList] = useState([]);

  const displayImages = async () => {
    const list = await ListImagesInBucket();
    setImageList(list);
    console.log('printed images')
  };

  const windowWidth = Dimensions.get('window').width; //sets size of displayed images depending on screen size
  const windowHeight = Dimensions.get('window').height;
  //const imageHeight = windowWidth; // images will be square

  return (
    <View style={styles.genericContainer}>
      <View style={styles.line} />
      <View style={styles.homeButtonContainer}>
        <TouchableOpacity onPress={displayImages}>
          <Text style={styles.settingsButtonText}>{"Click to load/refresh"}</Text>
        </TouchableOpacity>
      </View>

      <ScrollView>
        {imageList.map((imageUrl, index) => (
          <Image key={index} source={{ uri: imageUrl }} style={{ width: windowWidth, height: windowHeight, resizeMode: 'contain', marginBottom: 5 }} />
        ))}
      </ScrollView>
    </View>
  );
}

///////////////// Main //////////////////////////
const Stack = createNativeStackNavigator();

let ws;
function serverConnection() {
  const WS_URL = 'ws://192.168.8.207:8080'; // pi IP and user specified port
  ws = new WebSocket(WS_URL);
}

function App() {
  serverConnection();

  ws.onopen = () => {
    console.log('connected');
  }

  ws.addEventListener('message', function incoming(event) {
    const data = event.data;
    console.log('Message from Pi: ' + data);
  });


  return (
    <NavigationContainer>
      <Stack.Navigator screenOptions={{ headerShown: false }}>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="RobotControls" component={RobotControls} />
        <Stack.Screen name="CameraScreen" component={CameraScreen} />
        <Stack.Screen name="PhotoScreen" component={PhotoScreen} />
      </Stack.Navigator>
    </NavigationContainer >
  );
}

export default App;