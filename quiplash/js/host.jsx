import React from 'react';

class Host extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      players: [],
      stage: 0,
      answeredPlayers: [],
      votedPlayers: [],
    };

    this.handleStartButton = this.handleStartButton.bind(this);
    this.handleResetPlayers = this.handleResetPlayers.bind(this);

  }

  componentDidMount() {
    this.interval = setInterval(() => this.getPlayers(), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  handleResetPlayers() {
    fetch('/api/v1/resetplayers', {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'same-origin',
    })
  }

  getPlayers() {

    fetch('/api/v1/players', {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'same-origin',
    })
    .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      }).then((data) => {
        this.setState(prevState => ({
          players: data.players,
        }));
      })
      .catch();

      // Update answered players
      var ansPlayers = [];
      this.state.players.forEach(function(player) {
        if(player.ans1 !== "" && player.ans2 !== "") {
          ansPlayers.push(player)
        }
      });

      this.setState(prevState => ({
          answeredPlayers: ansPlayers,
        }));

      // Check if all players have answered
      if(this.state.answeredPlayers.length === this.state.players.length && this.state.answeredPlayers.length > 0) {
        // All players have answered, next stage
        this.setState(prevState => ({
          stage: 2,
        }));
      }

  }

  handleStartButton() {
    fetch('/api/v1/resetanswer', {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'same-origin',
    })

    this.setState(prevState => ({
          stage: 1,
          answeredPlayers: [],
        }));

  }


  render() {
    let output = ""
    switch(this.state.stage) {
      case 0:
        // Waiting for players
        output = (<div><p>Waiting for all players...</p>
          <ul>
            {
            this.state.players.map((player, index) =>
              <li key={index}><p>{player.name}</p></li>)
              }
          </ul>

        { this.state.players.length > 2 && 
          <button onClick={this.handleStartButton}>Start</button>
        }
        <button onClick={this.handleResetPlayers}>Reset</button>
        </div>);
        break;

      case 1:
        // Answering questions
        output = (<div><p>Waiting for players to answer questions...</p>

        <ul>
            {
            this.state.answeredPlayers.map((player, index) =>
              <li key={index}><p>{player.name}</p></li>)
              }
          </ul>
          </div>);

        break;

      case 2:
        // Display answers and wait for all votes
        output = (<div><p>Waiting for players to vote on questions...</p>

        <ul>
            {
            this.state.votedPlayers.map((player, index) =>
              <li key={index}><p>{player.name}</p></li>)
              }
          </ul>
          </div>);

        break;

      default:
        // code block
    }
    return (
      <div className="host">
        {output}
      </div>
    );
  }
}

Host.propTypes = {
};

export default Host;
