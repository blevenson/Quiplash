import React from 'react';

class Host extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      players: [],
    };

  }

  componentDidMount() {
  }


  render() {
    return (
      <div className="host">
        <p>Waiting for all players...</p>
        <ul>
          {
          this.props.players.map((player, index) =>
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
