import React from 'react';
import ProblemItem from './ProblemItem';
import '../styles/ProblemList.css';

/**
 * ProblemList Component
 * Displays a list of identified problems with proper semantic HTML
 */
function ProblemList({ items }) {
  if (!items || items.length === 0) {
    return (
      <div className="empty-results" role="status">
        <p>No challenges identified. Try analyzing different research text.</p>
      </div>
    );
  }

  return (
    <div className="problem-list" role="list" aria-label="List of identified challenges">
      {items.map((item, index) => (
        <ProblemItem 
          key={index} 
          item={item} 
          index={index}
          role="listitem"
        />
      ))}
    </div>
  );
}

export default ProblemList;
