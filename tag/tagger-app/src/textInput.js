import React from 'react'
import './textInput.css'

class TextAdd extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			value: this.props.defaultText,
			infoVisibility: 'invisible'
		};
	}

	handleFocus = () => {
		this.setState({ infoVisibility: 'visible' });
		if (this.state.value == this.props.defaultText) {
			this.setState({
				value: ''
			});
		}
	}

	handleBlur = () => {
		this.setState({ infoVisibility: 'invisible' });
		if (this.state.value == "") {
			this.setState({
				value: this.props.defaultText,
			});
		}
	}

	handleChange = (event) => {
		// process input
		this.setState({
			value: event.target.value
		});
	}

	checkSubmit = (event) => {
		if ((event.key === 'Enter') && (event.target.value != '')) {
			this.props.action(this.state.value);
			this.setState({
				value: ''
			});
		}
	}

	render() {
		return (
			<div>
				<input type="text" 
					value = {this.state.value} 
					onFocus = {this.handleFocus} 
					onBlur = {this.handleBlur} 
					onChange = {this.handleChange} 
					onKeyDown = {this.checkSubmit} />
				<div className={'info ' + this.state.infoVisibility}>
					Press <b>Enter</b> to submit
				</div>
			</div>
		);
	}
};

export default TextAdd