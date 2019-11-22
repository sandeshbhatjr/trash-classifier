import React from 'react';
import './tag.css';

// Create a component named Tag Component
class Tag extends React.Component {
	ontagClick() {
		return 1;
	}

	render() {
		return (
			<span key={this.props.tagName} className="tag {this.props.selected}">
				{' '}{this.props.tagName}{' '}
			</span>
		);
	}
};

export default Tag;
