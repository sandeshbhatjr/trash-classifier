import React from 'react';
import './imagedisplay.css'

class ImageDisplay extends React.Component {
	constructor(props) {
		super(props);
	}

	render() {
		return (
			<div className="img-container">
				<img src={this.props.imageURL} height='400px' />
				<div className="navigator">
					 <span className='hint'>(A)</span> <a>Prev.</a> &#160; ( 1 / 10 )  &#160; <a>Next</a> <span className='hint'>(D)</span>
					 <div className='hint'> Use keys to navigate</div>
				</div>
			</div>
		);
	}
}

export default ImageDisplay;