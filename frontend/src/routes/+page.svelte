<script>
	// 1. ใช้ Runes ($state) จัดการสถานะ activeTab
	let activeTab = $state('home');

	// 2. ปรับข้อมูลเป็น $state เพื่อให้แก้ไขคะแนนได้ (Two-way binding)
	// และเพิ่มฟิลด์ number ตามโจทย์
	let candidates = $state([
		{ number: 1, name: 'สมชาย รักชาติ', role: 'พรรคก้าวหน้า', votes: 12500, color: '#FF6B6B' },
		{ number: 2, name: 'สมหญิง จริงใจ', role: 'พรรคเพื่อไทย', votes: 15300, color: '#4ECDC4' },
		{ number: 3, name: 'ศักดิ์สิทธิ์ พัฒนา', role: 'พรรคประชา', votes: 9800, color: '#FFE66D' }
	]);

	// ปรับชื่อสมาชิกให้เป็นชื่อ-นามสกุลจริง
	let members = $state([
		{ number: 1, name: 'อำนวย ช่วยเหลือ', role: 'เขต 1', color: '#FF9F43', votes: 4500 },
		{ number: 2, name: 'บำรุง ท้องถิ่น', role: 'เขต 2', color: '#54A0FF', votes: 3200 },
		{ number: 3, name: 'จิตรา มั่นคง', role: 'เขต 3', color: '#5F27CD', votes: 5100 },
		{ number: 4, name: 'ประเสริฐ เลิศล้ำ', role: 'เขต 4', color: '#FF6B6B', votes: 1800 },
		{ number: 5, name: 'สุดา พาเจริญ', role: 'เขต 5', color: '#1DD1A1', votes: 4200 },
	]);

	// ฟังก์ชันจำลองการบันทึก
	function saveScore(name, score) {
		alert(`บันทึกคะแนนของ ${name}: ${score} เรียบร้อยแล้ว`);
	}

	// SVG Paths สำหรับไอคอน
	const icons = {
		home: "M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z M9 22V12h6v10",
		pm: "M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2 M12 3a4 4 0 1 0 0 8 4 4 0 0 0 0-8",
		members: "M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2 M16 3.13a4 4 0 0 1 0 7.75 M23 21v-2a4 4 0 0 0-3-3.87",
		score: "M18 20V10 M12 20V4 M6 20v6"
	};
</script>

<svelte:head>
	<!-- โหลดฟอนต์ Sarabun จาก Google Fonts -->
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;700&display=swap" rel="stylesheet">
</svelte:head>

<!-- 
    ========================================
    SNIPPETS SECTION
    ========================================
-->

<!-- Snippet 1: Navbar Item -->
{#snippet navItem(id, label, iconPath)}
	<button 
		class="nav-btn {activeTab === id ? 'active' : ''}" 
		onclick={() => activeTab = id}
	>
		<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
			<path d={iconPath} />
		</svg>
		<span>{label}</span>
	</button>
{/snippet}

<!-- Snippet 2: Home View -->
{#snippet viewHome()}
	<div class="page-content home-bg">
		<div class="hero">
			<h1>ระบบบันทึกคะแนน</h1>
			<p>กรุณาเลือกเมนู "นายกฯ" หรือ "สมาชิกฯ" เพื่อทำการกรอกคะแนน</p>
		</div>
		<div class="card">
			<h3>สถานะการส่งข้อมูล</h3>
			<p>หน่วยเลือกตั้งที่ 1: <span style="color: green">กำลังดำเนินการ</span></p>
		</div>
		<div class="card">
			<h3>คำแนะนำ</h3>
			<p>ตรวจสอบความถูกต้องของตัวเลขหน้าบัตรและคะแนนก่อนกดบันทึก</p>
		</div>
	</div>
{/snippet}

<!-- Snippet 3: PM View (กรอกคะแนน นายกฯ) -->
{#snippet viewPM()}
	<div class="page-content">
		<h2>บันทึกคะแนน นายกฯ</h2>
		<div class="list-container">
			{#each candidates as c}
				<div class="input-card">
					<div class="card-header">
						<!-- 1. รูป -->
						<div class="avatar-large" style="background-color: {c.color}">
							{c.name.charAt(0)}
						</div>
						<div class="header-info">
							<!-- 2. หมายเลข -->
							<div class="number-badge">เบอร์ {c.number}</div>
							<!-- 3. ชื่อ นามสกุล -->
							<h3>{c.name}</h3>
							<small>{c.role}</small>
						</div>
					</div>
					<div class="card-body compact">
						<div class="input-group">
							<label>คะแนน:</label>
							<input type="number" bind:value={c.votes} class="score-input" placeholder="0">
						</div>
						<button class="btn-save" onclick={() => saveScore(c.name, c.votes)}>
							บันทึก
						</button>
					</div>
				</div>
			{/each}
		</div>
	</div>
{/snippet}

<!-- Snippet 4: Members View (กรอกคะแนน สมาชิกฯ) -->
{#snippet viewMembers()}
	<div class="page-content">
		<h2>บันทึกคะแนน สมาชิกฯ</h2>
		<div class="list-container">
			{#each members as m}
				<div class="input-card">
					<div class="card-header">
						<!-- 1. รูป -->
						<div class="avatar-large" style="background-color: {m.color}">
							{m.name.split(' ')[1] ? m.name.split(' ')[1].charAt(0) : m.name.charAt(0)}
						</div>
						<div class="header-info">
							<!-- 2. หมายเลข -->
							<div class="number-badge member-badge">เบอร์ {m.number}</div>
							<!-- 3. ชื่อ นามสกุล -->
							<h3>{m.name}</h3>
							<small>{m.role}</small>
						</div>
					</div>
					<div class="card-body compact">
						<div class="input-group">
							<label>คะแนน:</label>
							<input type="number" bind:value={m.votes} class="score-input" placeholder="0">
						</div>
						<button class="btn-save" onclick={() => saveScore(m.name, m.votes)}>
							บันทึก
						</button>
					</div>
				</div>
			{/each}
		</div>
	</div>
{/snippet}

<!-- Snippet 5: Score View -->
{#snippet viewScore()}
	<div class="page-content">
		<h2>สรุปคะแนน Real-time</h2>
		
		<div class="section-header">
			<span class="icon">🏆</span>
			<h3>ผลคะแนน นายกฯ</h3>
		</div>
		<div class="chart-container card">
			{#each candidates as c}
				<!-- คำนวณ % เทียบกับ 30,000 (สมมติ) -->
				{@const percent = Math.min(100, Math.round((c.votes / 30000) * 100))}
				<div class="score-row">
					<div class="score-avatar" style="background-color: {c.color}">
						{c.number}
					</div>
					<div class="score-details">
						<div class="bar-label">
							<span class="name">{c.name}</span>
							<span class="count">{c.votes ? c.votes.toLocaleString() : 0}</span>
						</div>
						<div class="progress-bg">
							<div class="progress-fill" style="width: {percent}%; background-color: {c.color}"></div>
						</div>
					</div>
				</div>
			{/each}
		</div>

		<div class="section-header mt-4">
			<span class="icon">👥</span>
			<h3>ผลคะแนน สมาชิกฯ</h3>
		</div>
		<div class="chart-container card">
			{#each members as m}
				<!-- คำนวณ % เทียบกับ 10,000 (สมมติ) -->
				{@const percent = Math.min(100, Math.round((m.votes / 10000) * 100))}
				<div class="score-row">
					<div class="score-avatar" style="background-color: {m.color}">
						{m.number}
					</div>
					<div class="score-details">
						<div class="bar-label">
							<span class="name">{m.name}</span>
							<span class="count">{m.votes ? m.votes.toLocaleString() : 0}</span>
						</div>
						<div class="progress-bg">
							<div class="progress-fill" style="width: {percent}%; background-color: {m.color}"></div>
						</div>
					</div>
				</div>
			{/each}
		</div>
	</div>
{/snippet}


<!-- 
    ========================================
    MAIN LAYOUT
    ========================================
-->
<main class="app-container">
	<!-- Top Bar -->
	<header class="top-bar">
		<div class="logo">E-Vote Rec</div>
		<div class="user-profile">
			<div class="circle"></div>
		</div>
	</header>

	<!-- Content Area -->
	<div class="content-area">
		{#if activeTab === 'home'}
			{@render viewHome()}
		{:else if activeTab === 'pm'}
			{@render viewPM()}
		{:else if activeTab === 'members'}
			{@render viewMembers()}
		{:else if activeTab === 'score'}
			{@render viewScore()}
		{/if}
	</div>

	<!-- Bottom Navigation Bar -->
	<nav class="bottom-nav">
		{@render navItem('home', 'หน้าแรก', icons.home)}
		{@render navItem('pm', 'นายกฯ', icons.pm)}
		{@render navItem('members', 'สมาชิกฯ', icons.members)}
		{@render navItem('score', 'สรุปคะแนน', icons.score)}
	</nav>
</main>


<!-- 
    ========================================
    STYLES
    ========================================
-->
<style>
	:global(*) { box-sizing: border-box; }
	:global(body) {
		margin: 0; padding: 0;
		font-family: 'Sarabun', sans-serif;
		background-color: #f5f7fa;
		color: #333;
		overflow: hidden;
		position: fixed; width: 100%; height: 100%;
	}

	.app-container {
		display: flex; flex-direction: column;
		height: 100vh; height: 100dvh;
		width: 100%; max-width: 600px;
		margin: 0 auto; background-color: #fff;
		position: relative; overflow: hidden;
	}

	.top-bar {
		height: 60px; background: #fff;
		display: flex; align-items: center; justify-content: space-between;
		padding: 0 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);
		z-index: 10; flex-shrink: 0;
	}
	.top-bar .logo { font-weight: 700; font-size: 1.2rem; color: #2c3e50; }
	.user-profile .circle { width: 35px; height: 35px; background-color: #ddd; border-radius: 50%; }

	.content-area {
		flex: 1; overflow-y: auto; -webkit-overflow-scrolling: touch;
		background-color: #f8f9fa; position: relative;
		padding-bottom: 20px;
	}
	.page-content { padding: 20px; animation: fadeIn 0.3s ease; }
	@keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }

	h1, h2, h3 { margin-top: 0; }
	.card {
		background: white; padding: 15px; border-radius: 12px;
		margin-bottom: 15px; box-shadow: 0 2px 5px rgba(0,0,0,0.03);
	}

	/* --- Input Card Style --- */
	.input-card {
		background: white;
		border-radius: 16px;
		margin-bottom: 15px;
		box-shadow: 0 2px 8px rgba(0,0,0,0.05);
		border: 1px solid #f0f0f0;
		overflow: hidden;
	}
	.card-header {
		display: flex;
		align-items: center;
		padding: 15px; /* รูปและชื่อเด่น */
		background-color: #fdfdfd;
		border-bottom: 1px solid #eee;
	}
	.avatar-large {
		width: 60px; height: 60px;
		border-radius: 50%;
		display: flex; align-items: center; justify-content: center;
		color: white; font-weight: bold; font-size: 1.5rem;
		margin-right: 15px; flex-shrink: 0;
		box-shadow: 0 2px 5px rgba(0,0,0,0.1);
	}
	.header-info { flex: 1; }
	.header-info h3 { margin: 5px 0 0; font-size: 1.1rem; color: #333; }
	.header-info small { color: #888; }
	
	.number-badge {
		display: inline-block;
		background: #2c3e50; color: white;
		padding: 2px 8px; border-radius: 4px;
		font-size: 0.75rem; font-weight: bold;
	}
	.member-badge { background: #576574; }

	.card-body {
		padding: 12px 15px; /* ลด padding ลง */
		display: flex; align-items: flex-end; justify-content: space-between;
		gap: 10px;
		background-color: #fafafa;
	}
	.input-group { flex: 1; display: flex; flex-direction: column; }
	.input-group label { font-size: 0.75rem; color: #888; margin-bottom: 2px; }
	
	.score-input {
		width: 100%; padding: 6px 10px; /* ปรับขนาด Input เล็กลง */
		font-size: 1rem; font-family: 'Sarabun'; /* ลดขนาดตัวอักษร */
		border: 1px solid #ddd; border-radius: 6px;
		text-align: left; color: #2c3e50; font-weight: bold;
		background: #fff;
		transition: border-color 0.2s;
	}
	.score-input:focus { border-color: #3498db; outline: none; }

	.btn-save {
		background: #27ae60; color: white;
		border: none; padding: 0 15px;
		height: 36px; /* ลดความสูงปุ่มลง (จาก 48px) */
		font-size: 0.85rem; /* ลดขนาดตัวอักษรปุ่ม */
		border-radius: 6px; font-family: 'Sarabun';
		font-weight: bold; cursor: pointer;
		display: flex; align-items: center;
		box-shadow: 0 2px 4px rgba(39, 174, 96, 0.2);
		flex-shrink: 0;
	}
	.btn-save:active { transform: translateY(1px); }

	/* --- Score Styles --- */
	.section-header { display: flex; align-items: center; margin-bottom: 10px; }
	.section-header .icon { margin-right: 8px; font-size: 1.2rem; }
	.section-header h3 { margin: 0; font-size: 1.1rem; color: #2c3e50; }
	.mt-4 { margin-top: 20px; }
	.score-row { display: flex; align-items: center; margin-bottom: 15px; }
	.score-avatar {
		width: 40px; height: 40px; border-radius: 50%;
		display: flex; align-items: center; justify-content: center;
		color: white; font-weight: bold; font-size: 1rem;
		margin-right: 12px; flex-shrink: 0;
	}
	.score-details { flex: 1; }
	.bar-label { display: flex; justify-content: space-between; margin-bottom: 5px; font-size: 0.9rem; }
	.progress-bg { background: #eee; height: 8px; border-radius: 4px; overflow: hidden; }
	.progress-fill { height: 100%; transition: width 0.5s ease; border-radius: 4px; }

	/* --- Bottom Nav --- */
	.bottom-nav {
		height: 70px; background: #fff; border-top: 1px solid #eee;
		display: flex; justify-content: space-around; align-items: center;
		padding-bottom: env(safe-area-inset-bottom);
		flex-shrink: 0; z-index: 20;
	}
	.nav-btn {
		background: none; border: none; padding: 0;
		display: flex; flex-direction: column; align-items: center; justify-content: center;
		color: #95a5a6; cursor: pointer; font-family: 'Sarabun';
		width: 100%; height: 100%;
	}
	.nav-btn svg { margin-bottom: 4px; transition: transform 0.2s; }
	.nav-btn span { font-size: 0.75rem; font-weight: 500; }
	.nav-btn.active { color: #3498db; }
	.nav-btn.active svg { transform: translateY(-2px); }
</style>