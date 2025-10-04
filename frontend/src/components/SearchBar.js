import React, { useState } from 'react';

const SearchBar = ({ onAnalyze, onSearch, placeholder, isLoading, mode }) => {
  const [inputValue, setInputValue] = useState('');
  const [isExpanded, setIsExpanded] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!inputValue.trim()) return;

    if (mode === 'analyze') {
      onAnalyze(inputValue);
    } else {
      onSearch(inputValue);
    }
  };

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleClear = () => {
    setInputValue('');
    setIsExpanded(false);
  };

  const handleFocus = () => {
    setIsExpanded(true);
  };

  const handleBlur = () => {
    // Delay collapse to allow for clicking on buttons
    setTimeout(() => setIsExpanded(false), 200);
  };

  return (
    <div className="search-bar-container">
      <form 
        onSubmit={handleSubmit} 
        className="search-form"
        role="search"
        aria-label="Search and analyze research"
      >
        <div className="search-input-group">
          <label htmlFor="search-input" className="visually-hidden">
            {mode === 'analyze' ? 'Research text to analyze' : 'Search terms'}
          </label>
          <textarea
            id="search-input"
            className="search-input"
            value={inputValue}
            onChange={handleInputChange}
            onFocus={handleFocus}
            onBlur={handleBlur}
            placeholder={placeholder}
            rows={isExpanded ? 6 : 2}
            disabled={isLoading}
            aria-describedby="search-help"
            aria-multiline="true"
          />
          <div id="search-help" className="search-help">
            {mode === 'analyze' 
              ? 'Paste research text, abstracts, or paper excerpts to analyze for relevant issues.'
              : 'Enter keywords to search through previously analyzed issues.'
            }
          </div>
        </div>

        <div className="search-actions">
          <button
            type="submit"
            className="search-button primary"
            disabled={isLoading || !inputValue.trim()}
            aria-describedby="search-help"
          >
            {isLoading ? (
              <>
                <span className="spinner" aria-hidden="true"></span>
                {mode === 'analyze' ? 'Analyzing...' : 'Searching...'}
              </>
            ) : (
              mode === 'analyze' ? 'Analyze Text' : 'Search Issues'
            )}
          </button>

          {inputValue && (
            <button
              type="button"
              className="search-button secondary"
              onClick={handleClear}
              aria-label="Clear search input"
            >
              Clear
            </button>
          )}
        </div>
      </form>

      {mode === 'analyze' && (
        <div className="analysis-tips" role="region" aria-label="Analysis tips">
          <h3>Tips for Better Analysis:</h3>
          <ul>
            <li>Include abstracts, methodology, and results sections</li>
            <li>Focus on studies involving your selected user group</li>
            <li>Include discussion sections that mention challenges or barriers</li>
            <li>Longer text generally provides more comprehensive results</li>
          </ul>
        </div>
      )}
    </div>
  );
};

export default SearchBar;