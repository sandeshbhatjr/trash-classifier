import React from 'react';
import Tag from './tag'
import './tag_collection.css';

// Create a component named Tag Component
class TagCollection extends React.Component {
	render() {
		const {tags} = this.props;

		const renderedTags = this.props.tags.map((tagname) => {
			return(
				<Tag tagName={tagname} />
			);	
		});

		return (
			<div className='tags'>
				{renderedTags}
			</div>
		);
	}
};

export default TagCollection;
