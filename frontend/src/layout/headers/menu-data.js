const menu_data = [
  {
    id: 1,
    mega_menu: false,
    title: "Home",
    link: "/",
    active: "active",
    sub_menus: [
      { link: "/", title: "Data analytics" },
    ],
  },
  {
    id: 2,
    mega_menu: false,
    title: "Pages",
    link: "/about",
    active: "",
    sub_menus: [
      { link: "/about", title: "About" },
      
    ],
  },
  
  {
    id: 3,
    mega_menu: false,
    title: "Projects",
    link: "/project",
    active: "",
    sub_menus: [
      { link: "/project", title: "Project" },
      { link: "/project-details", title: "Project Details" }, 
    ],
  },
  {
    id: 4,
    mega_menu: false,
    has_dropdown: false,
    title: "Contact",
    link: "/contact",
    active: "",
  },
  

];
export default menu_data;
