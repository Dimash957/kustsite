import { useState } from 'react'
import './App.css'
import SearchBar from './components/SearchBar'
import FilterGroup from './components/FilterGroup'
import ProblemList from './components/ProblemList'
import { analyzeText } from './services/api'

function App() {
  const [problems, setProblems] = useState([])
  const [group, setGroup] = useState('People with disabilities')
  const [category, setCategory] = useState('Accessibility')
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState('')

  async function handleSearch(query) {
    try {
      setIsLoading(true)
      setError('')
      const issues = await analyzeText(query, group, category)
      setProblems(issues)
    } catch (err) {
      setError(err?.message || 'Failed to analyze text')
      setProblems([])
    } finally {
      setIsLoading(false)
    }
  }

  const groupOptions = ['People with disabilities', 'Elderly', 'Students']
  const categoryOptions = ['Accessibility', 'Mobility', 'Cognitive', 'Mental health']

  return (
    <div className="App">
      <header>
        <h1>Research Challenges by Group</h1>
        <p className="subtitle">AI-assisted summaries of problems documented in scientific literature</p>
      </header>

      <SearchBar onSearch={handleSearch} placeholder="Paste an abstract or enter a query…" />

      <section aria-labelledby="filters-heading" className="filters-section">
        <h2 id="filters-heading" className="visually-hidden">Filters</h2>
        <div className="filters">
          <FilterGroup label="User Group" options={groupOptions} value={group} onChange={setGroup} />
          <FilterGroup label="Problem Category" options={categoryOptions} value={category} onChange={setCategory} />
        </div>
      </section>

      <ProblemList items={problems} isLoading={isLoading} error={error} />
    </div>
  )
}

export default App
