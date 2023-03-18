import { useState, useEffect } from 'react';
import './App.css';
import './style.css';
import pluData from './pluData.json';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';


function App() {
  const [searchTerm, setSearchTerm] = useState('');
  const [pluCode, setPluCode] = useState('');
  const [suggestions, setSuggestions] = useState([]);
  
  const updateSuggestions = () => {
    if (searchTerm.trim() === ''){
      setSuggestions([]);
      return;
    }

    const searchRegExp = new RegExp(searchTerm, 'i');
    const filteredSuggestions = pluData.filter((data) => 
    searchRegExp.test(data.item)
    );

    setSuggestions(filteredSuggestions.slice(0,5));

  };
  
  useEffect(() => {
    updateSuggestions();
  }, [searchTerm]);


  
  const handleSearch = () => {
    const produceItem = pluData.find(
      (data) => data.item.toLowerCase() === searchTerm.toLowerCase()
    );
    if (produceItem) {
      setPluCode(produceItem.plu);
    } else {
      setPluCode('No PLU code found');
    }
  };

  const handleSuggestionClick = (item, plu) => {
    setSearchTerm(item);
    setPluCode(plu);
    setSuggestions([]);
  };

  return (
    <div className="App">
      <h1>Produce PLU Code Search</h1>
<section className='search-area'>

  <label htmlFor='produce-search'>Search for produce item by name</label>
      <input
        type="text"
        id="produce-search"
        placeholder="Enter produce item"
        value={searchTerm}
        onChange={(e) => {
          setSearchTerm(e.target.value);
          if (e.target.value === ''){
            setPluCode('');
            }
          }
        }
      />
      <button 
      type="submit"
      onClick={handleSearch} 
      className="search-icon-button"
      aria-label='Search'>
        <FontAwesomeIcon icon={faSearch} />
      </button>
      </section>
      <ul className='suggestions-list'>
        {suggestions.map((suggestion) => (
          <li
          key={suggestion.plu}
          onClick={() => handleSuggestionClick(suggestion.item, suggestion.plu)}
          >
            {suggestion.item}
          </li>
        ))}
      </ul>
      <p className={pluCode ? 'plu-result' : ''}>
        {pluCode ? `PLU Code: ${pluCode}` : ''}
        </p>
{/*   {pluCode && <div>PLU Code: {pluCode}</div>}
 */}    </div>
    
  );
}

export default App;
