<style>
    /* GitHub 다크 모드 배경색과 어울리도록 텍스트 색상 설정 */
    body {
        font-family: 'Inter', sans-serif; /* Inter 폰트는 GitHub에서 지원하지 않을 수 있으나, 기본 폰트로 대체됩니다. */
        color: #c9d1d9; /* GitHub 다크 모드 텍스트 색상 */
    }
    /* 뱃지 이미지에 대한 커스텀 스타일 (일관된 크기 및 둥근 모서리) */
    .badge-img {
        border-radius: 0.5rem; /* 둥근 모서리 */
        transition: transform 0.2s ease-in-out; /* 부드러운 전환 효과 */
    }
    .badge-img:hover {
        transform: translateY(-2px); /* 호버 시 약간 위로 이동 */
    }
    /* GitHub README에서 Tailwind CSS 클래스가 직접 적용되지 않으므로, 일부 스타일은 수동으로 적용해야 합니다. */
    /* 아래 클래스들은 Tailwind 클래스이지만, GitHub README에서는 직접 작동하지 않을 수 있습니다. */
    /* 필요하다면 이 스타일을 인라인으로 각 요소에 직접 적용하거나, GitHub에서 지원하는 기본 Markdown/HTML로 대체해야 합니다. */
    .text-center { text-align: center; }
    .mb-10 { margin-bottom: 2.5rem; }
    .mb-6 { margin-bottom: 1.5rem; }
    .mb-4 { margin-bottom: 1rem; }
    .text-4xl { font-size: 2.25rem; } /* 36px */
    .md\:text-5xl { /* 미디어 쿼리는 GitHub에서 작동하지 않습니다. */ }
    .font-bold { font-weight: 700; }
    .text-white { color: #ffffff; }
    .text-lg { font-size: 1.125rem; } /* 18px */
    .md\:text-xl { /* 미디어 쿼리는 GitHub에서 작동하지 않습니다. */ }
    .text-gray-400 { color: #9ca3af; }
    .text-3xl { font-size: 1.875rem; } /* 30px */
    .font-semibold { font-weight: 600; }
    .text-gray-300 { color: #d1d5db; }
    .flex { display: flex; }
    .flex-wrap { flex-wrap: wrap; }
    .justify-center { justify-content: center; }
    .gap-4 { gap: 1rem; }
    .block { display: block; }
    .max-w-4xl { max-width: 56rem; } /* 896px */
    .mx-auto { margin-left: auto; margin-right: auto; }
    .bg-\[\#161b22\] { background-color: #161b22; }
    .p-6 { padding: 1.5rem; }
    .md\:p-8 { /* 미디어 쿼리는 GitHub에서 작동하지 않습니다. */ }
    .lg\:p-10 { /* 미디어 쿼리는 GitHub에서 작동하지 않습니다. */ }
    .rounded-xl { border-radius: 0.75rem; }
    .shadow-lg { box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); }
    .w-full { width: 100%; }
    .max-w-xl { max-width: 36rem; } /* 576px */
    .rounded-lg { border-radius: 0.5rem; }
    .shadow-md { box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); }
</style>

<div class="max-w-4xl mx-auto bg-[#161b22] p-6 rounded-xl shadow-lg">

    <!-- 헤더 섹션 -->
    <header class="text-center mb-10">
        <h1 class="text-4xl font-bold text-white mb-2">
            안녕하세요, d5ngjun2입니다! 👋
        </h1>
        <p class="text-lg text-gray-400">
            영향력 있는 소프트웨어 솔루션 개발에 열정적입니다.
        </p>
    </header>

    <!-- 연락처 섹션 -->
    <section class="mb-10">
        <h2 class="text-3xl font-semibold text-white mb-6 text-center">🧑‍💻 Contact Me 🧑‍💻</h2>
        <div class="flex flex-wrap justify-center gap-4 mb-4">
            <a href="https://nikihwangg.tistory.com/" target="_blank" rel="noopener noreferrer" class="block">
                <img src="https://img.shields.io/badge/Tistory-000000?style=for-the-badge&logo=Tistory&logoColor=white" alt="Tistory" class="badge-img">
            </a>
            <a href="mailto:nikihwangg@ivycomtech.com" class="block">
                <img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=Gmail&logoColor=white" alt="Gmail" class="badge-img">
            </a>
            <a href="https://www.instagram.com/exdwxn__" target="_blank" rel="noopener noreferrer" class="block">
                <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=Instagram&logoColor=white" alt="Instagram" class="badge-img">
            </a>
            <a href="https://notion.so" target="_blank" rel="noopener noreferrer" class="block">
                <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white" alt="Notion" class="badge-img">
            </a>
        </div>
        <p class="text-center text-gray-300 text-lg">
            <strong>📧 이메일:</strong> nikihwangg@ivycomtech.com
        </p>
    </section>

    <!-- 기술 스택 섹션 -->
    <section class="mb-10">
        <h2 class="text-3xl font-semibold text-white mb-6 text-center">✨ Tech Stack ✨</h2>
        <div class="flex flex-wrap justify-center gap-4">
            <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white" alt="Python" class="badge-img">
            <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white" alt="MySQL" class="badge-img">
            <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=for-the-badge&logo=Amazon%20AWS&logoColor=white" alt="Amazon AWS" class="badge-img">
            <img src="https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=Java&logoColor=white" alt="Java" class="badge-img">
            <img src="https://img.shields.io/badge/Spring-6DB33F?style=for-the-badge&logo=Spring&logoColor=white" alt="Spring" class="badge-img">
            <img src="https://img.shields.io/badge/Spring Boot-6DB33F?style=for-the-badge&logo=Spring%20Boot&logoColor=white" alt="Spring Boot" class="badge-img">
            <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white" alt="Git" class="badge-img">
            <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white" alt="GitHub" class="badge-img">
        </div>
    </section>

    <!-- GitHub 통계 섹션 -->
    <section>
        <h2 class="text-3xl font-semibold text-white mb-6 text-center">📊 GitHub Stats 📊</h2>
        <div class="flex justify-center">
            <img src="https://github-readme-stats.vercel.app/api?username=d5ngjun2&show_icons=true&theme=radical&hide_border=true" alt="GitHub Stats" class="w-full max-w-xl rounded-lg shadow-md">
        </div>
    </section>

</div>
