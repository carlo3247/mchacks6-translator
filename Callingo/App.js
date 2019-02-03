import React from 'react';
import call from 'react-native-phone-call';
import { StyleSheet, Text, View, Button } from 'react-native';


export default class App extends React.Component {
  call = () => {
    //handler to make a call
    const args = {
      number: '2262864476',
      prompt: false,
    };
 
    call(args).catch(console.error);
  };
  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.bigBlue}>CALLINGO</Text>
        <Text style={styles.reddd}>Offline Conversation Translator</Text>
        <Text style={styles.reddd}></Text>
        <Text style={styles.redd}>226-286-4476</Text>
        <View style={styles.redd}>
        <Button title="Make a call" onPress={this.call} />
        </View>
        <Text style={styles.reddd}></Text>
        <Text style={styles.reddd}>Chinese</Text>
        <Text style={styles.reddd}>Danish</Text>
        <Text style={styles.reddd}>Dutch</Text>
        <Text style={styles.reddd}>Finnish</Text>
        <Text style={styles.reddd}>French</Text>
        <Text style={styles.reddd}>Italian</Text>
        <Text style={styles.reddd}>Japanese</Text>
        <Text style={styles.reddd}>Korean</Text>
        <Text style={styles.reddd}>Norwegian</Text>
        <Text style={styles.reddd}>Polish</Text>
        <Text style={styles.reddd}>Portuguese</Text>
        <Text style={styles.reddd}>English</Text>
        <Text style={styles.reddd}>Russian</Text>
        <Text style={styles.reddd}>Spanish</Text>
        <Text style={styles.reddd}>Swedish</Text>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
    alignItems: 'center',
    justifyContent: 'center',
  },
  bigBlue: {
    color: '#2D6ED4',
    fontWeight: 'bold',
    fontSize: 55,
  },
  redd: {
    color: '#E692AA',
    fontWeight: 'bold',
    fontSize: 35,
  },
  reddd: {
    color: 'black',
    fontWeight: 'bold',
    fontSize: 18,
  },
});
