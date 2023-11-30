// @ts-check
import React, { useMemo, useState } from "react";
import ChatListItem from "./components/ChatListItem";
import Footer from "./components/Footer";

const ChatList = ({ rooms, dispatch, user, currentRoom, onLogOut }) => {
  const [searchInput, setSearchInput] = useState("");
  const countries = [
   
    { name: "Belgium", continent: "Europe" },
    { name: "India", continent: "Asia" },
    { name: "Bolivia", continent: "South America" },
    { name: "Ghana", continent: "Africa" },
    { name: "Japan", continent: "Asia" },
    { name: "Canada", continent: "North America" },
    { name: "New Zealand", continent: "Australasia" },
    { name: "Italy", continent: "Europe" },
    { name: "South Africa", continent: "Africa" },
    { name: "China", continent: "Asia" },
    { name: "Paraguay", continent: "South America" },
    { name: "Usa", continent: "North America" },
    { name: "France", continent: "Europe" },
    { name: "Botswana", continent: "Africa" },
    { name: "Spain", continent: "Europe" },
    { name: "Senegal", continent: "Africa" },
    { name: "Brazil", continent: "South America" },
    { name: "Denmark", continent: "Europe" },
    { name: "Mexico", continent: "South America" },
    { name: "Australia", continent: "Australasia" },
    { name: "Tanzania", continent: "Africa" },
    { name: "Bangladesh", continent: "Asia" },
    { name: "Portugal", continent: "Europe" },
    { name: "Pakistan", continent: "Asia" },
  
  ];
  const handleChange = (e) => {
    e.preventDefault();
    console.log(e)
    setSearchInput(e.target.value);
  };
    
  if (searchInput.length > 3) {
      console.log('x');
      countries.filter((country) => {
      return country.name.match(searchInput);
  });
  }
  const processedRooms = useMemo(() => {
   
    
    const roomsList = Object.values(rooms);
    const main = roomsList.filter((x) => x.id === "0");
    let other = roomsList.filter((x) => x.id !== "0");
    other = other.sort(
      (a, b) => +a.id.split(":").pop() - +b.id.split(":").pop()
    );
    return [...(main ? main : []), ...other];
  }, [rooms]);
  return (
    <>
      <div className="chat-list-container flex-column d-flex pr-4">
        <div className="py-2 px-2">
          <input
            type="text"
            placeholder="Search contacts"
            onChange={handleChange}
            className="form-control-search chat-input"
            value={searchInput} />
        </div>
        <div className="messages-box flex flex-1">
          <div className="list-group rounded-0">
            {processedRooms.map((room) => (
              <ChatListItem
                key={room.id}
                onClick={() =>
                  dispatch({ type: "set current room", payload: room.id })
                }
                active={currentRoom === room.id}
                room={room}
              />
            ))}
          </div>
        </div>
        <Footer user={user} onLogOut={onLogOut} />
      </div>
    </>
  );
};

export default ChatList;
