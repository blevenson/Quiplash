import React from 'react';

class Host extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      players: [],
    };

  }

  componentDidMount() {
    this.interval = setInterval(() => this.getPlayers(), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
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

  }


  render() {
    return (
      <div className="host">
        <p>Waiting for all players...</p>
        <ul>
          {
          this.state.players.map((player, index) =>
            <li key={index}><p>{player.name}</p></li>)
            }
        </ul>
      </div>
    );
  }
}

Host.propTypes = {
};

export default Host;
