import NavBar from "./NavBar";

export default function Layout({ children }) {
	return (
		<div>
			<div id="header" className="w-screen p-4 shadow-xl flex justify-between items-center">
				<div className="font-['Indie_Flower'] text-4xl">underStanding</div>
				<NavBar></NavBar>
			</div>
			<div className="flex border-solid border-1 border-sky-500 flex-col w-full mx-auto">
				{children}
			</div>
		</div>
	);
}
