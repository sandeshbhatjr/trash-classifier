import React from 'react';
import TagCollection from './tag_collection'
import TextAdd from './textInput'
import './tagger.css'

// Create a component named Tag Component
class Tagger extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			relevance: new Set([ 'relevant', 'irrelevant' ])
		};
	}

	addTag = (tagName, category) => {
		this.setState((state) => {
			return ({
				[category] : new Set(state[category]).add(tagName)
			});
		});
	}

	addCategory = (categoryName, defaultTag) => {
		this.setState((state) => {
			return ({
				[categoryName] : new Set([ defaultTag ])
			});
		});
	}

  	render() {
  		const allCategories = Object.keys(this.state).map((category) => {
			return (
				<div className="tag_collection">
					<div key={category} className="category_name">{category}</div>
					<TagCollection tags={Array.from(this.state[category])} />
					<TextAdd defaultText="+ Add Tag" action={tagName => {this.addTag(tagName, category)}} />
				</div>
			);
  		});
		return (
			<div className='tagger'>
				<div className='tag_collection_header'>
					SophisTagger 0.1 
					<div className='load_file_div'>+ Add data &#160; -- Save a copy</div>
				</div>
				{allCategories}
				<div className="tag_collection_last">
					<TextAdd defaultText="+ Add Category" action={categoryName => {this.addCategory(categoryName, 'default')}}/>
					<div className='derived_categories'> 
						You can also add derived categories as follows:<br/>
						<b>A x B</b> (product sets), <b>A U B</b> (union of sets)
					</div>
				</div>
			</div>
		);
	}
};

export default Tagger;
