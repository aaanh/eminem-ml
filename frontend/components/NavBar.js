import { Router } from "next/router";

function NavButton({ href, label, onClick }) {
	return (
		<a
			href={href}
			className="text-gray-500 hover:text-gray-700 transition-colors duration-200 ease-in-out flex justify-center items-center px-2 py-1 rounded-lg border"
			onClick={onClick}
		>
			{label}
		</a>
	);
}

export default function NavBar() {
	return (
		<div className="flex space-x-2">
			<NavButton href="/about" label="About" />
			<NavButton href="/about" label="About" />
			<NavButton href="/about" label="About" />
			<NavButton href="/about" label="About" />
		</div>
	);
}
