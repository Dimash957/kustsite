import React, { useState } from 'react';
import ProblemItem from './ProblemItem';

const ProblemList = ({ items, title, emptyMessage }) => {
  const [expandedItems, setExpandedItems] = useState(new Set());

  const toggleExpanded = (itemId) => {
    const newExpanded = new Set(expandedItems);
    if (newExpanded.has(itemId)) {
      newExpanded.delete(itemId);
    } else {
      newExpanded.add(itemId);
    }
    setExpandedItems(newExpanded);
  };

  if (!items || items.length === 0) {
    return (
      <div className="problem-list empty" role="status" aria-live="polite">
        <h2 className="problem-list-title">{title}</h2>
        <p className="empty-message">{emptyMessage}</p>
      </div>
    );
  }

  return (
    <div className="problem-list" role="region" aria-label="Research issues">
      <h2 className="problem-list-title">{title}</h2>
      <p className="problem-count" aria-live="polite">
        Found {items.length} {items.length === 1 ? 'issue' : 'issues'}
      </p>
      
      <ul className="problem-items" role="list">
        {items.map((item, index) => (
          <li key={item.id || index} className="problem-item-wrapper">
            <ProblemItem
              item={item}
              isExpanded={expandedItems.has(item.id || index)}
              onToggleExpanded={() => toggleExpanded(item.id || index)}
            />
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProblemList;