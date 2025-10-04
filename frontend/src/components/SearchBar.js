import React, { useState, useRef } from 'react';
import '../styles/SearchBar.css';

/**
 * SearchBar Component
 * Accessible search input with proper ARIA labels and keyboard support
 */
function SearchBar({ onSearch, placeholder = "Search...", disabled = false }) {
  const [query, setQuery] = useState('');
  const textareaRef = useRef(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim() && !disabled) {
      onSearch(query);
    }
  };

  const handleClear = () => {
    setQuery('');
    textareaRef.current?.focus();
  };

  return (
    <form 
      className="search-bar" 
      onSubmit={handleSubmit}
      role="search"
      aria-label="Research text analysis"
    >
      <div className="search-input-group">
        <label htmlFor="research-text-input" className="search-label">
          Research Text or Abstract
          <span className="required-indicator" aria-label="required">*</span>
        </label>
        
        <textarea
          ref={textareaRef}
          id="research-text-input"
          className="search-textarea"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder={placeholder}
          disabled={disabled}
          rows="8"
          aria-describedby="search-help-text"
          aria-required="true"
          required
        />
        
        <p id="search-help-text" className="help-text">
          Paste an abstract or excerpt from a research paper. The AI will analyze it to identify challenges.
        </p>
      </div>

      <div className="search-actions">
        <button
          type="submit"
          className="btn btn-primary"
          disabled={disabled || !query.trim()}
          aria-label="Analyze research text"
        >
          {disabled ? 'Analyzing...' : 'Analyze Text'}
        </button>
        
        {query && (
          <button
            type="button"
            className="btn btn-secondary"
            onClick={handleClear}
            disabled={disabled}
            aria-label="Clear search input"
          >
            Clear
          </button>
        )}
      </div>
    </form>
  );
}

export default SearchBar;
