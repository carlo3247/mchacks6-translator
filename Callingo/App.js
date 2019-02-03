import React from 'react';
import { StyleSheet, Text, View } from 'react-native';


export default class App extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.bigBlue}>CALLINGO</Text>
        <Text style={styles.reddd}>Offline Conversation Translator</Text>
        <Text style={styles.reddd}></Text>
        <Text style={styles.redd}>226-286-4476</Text>
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
    backgroundColor: '#020004',
    alignItems: 'center',
    justifyContent: 'center',
  },
  bigBlue: {
    color: 'yellow',
    fontWeight: 'bold',
    fontSize: 50,
  },
  redd: {
    color: 'red',
    fontWeight: 'bold',
    fontSize: 20,
  },
  reddd: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 10,
  },
});
