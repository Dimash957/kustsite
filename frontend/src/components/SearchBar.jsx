import { useState } from 'react'

export default function SearchBar({ onSearch, placeholder = 'Search articles, titles, or paste text…' }) {
  const [queryText, setQueryText] = useState('')

  function handleSubmit(event) {
    event.preventDefault()
    const trimmed = queryText.trim()
    if (trimmed.length > 0) {
      onSearch?.(trimmed)
    }
  }

  return (
    <form role="search" aria-label="Research search" onSubmit={handleSubmit} className="search-bar">
      <label htmlFor="search-input" className="search-label">Search articles</label>
      <div className="search-controls">
        <input
          id="search-input"
          type="text"
          value={queryText}
          onChange={(e) => setQueryText(e.target.value)}
          placeholder={placeholder}
          aria-describedby="search-help"
        />
        <button type="submit" className="button">Analyze</button>
      </div>
      <p id="search-help" className="visually-hidden">Enter search terms, a paper title, or paste an abstract.</p>
    </form>
  )
}