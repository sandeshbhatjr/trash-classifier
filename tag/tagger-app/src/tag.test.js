import React from 'react';
import ReactDOM from 'react-dom';
import taggerUnit from './tagger-unit';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
  ReactDOM.unmountComponentAtNode(div);
});
