import Head from "next/head";

export default function SEO({ title, description }) {
	return (
		<Head>
			<title>{title}</title>
			<link rel="icon" href="/favicon.ico" type="image/x-icon"></link>
			<meta
				name="description"
				content={description ? description : "A Stan's gotta do what a Stan gotta do."}
			/>
			<meta property="og:title" content="underSTANding Eminem" />
			<meta property="og:image" content="/favicon.ico" />
		</Head>
	);
}
