(() => {
  const variant = document.body.dataset.variant;
  const isSkilled = variant === "skilled";

  const glyphs = {
    application: "申",
    documents: "▤",
    family: "家",
    health: "＋",
    tax: "￥",
    notification: "●",
    search: "⌕",
    complete: "✓",
    attention: "!",
    update: "↻",
    me: "人",
  };

  const icon = (name, className = "") => {
    if (isSkilled) {
      return `<img class="ui-icon ${className}" src="assets/icons/${name}_line.svg" alt="">`;
    }
    return `<span class="generic-icon ${className}" aria-hidden="true">${glyphs[name]}</span>`;
  };

  const rows = [
    { id: "AP-2026-07131", name: "佐藤 美咲", kana: "サトウ ミサキ", kind: "子育て給付", received: "7月13日 16:42", status: "waiting", statusText: "確認待ち", owner: "高橋", due: "本日" },
    { id: "AP-2026-07130", name: "田中 健一", kana: "タナカ ケンイチ", kind: "住民票交付", received: "7月13日 15:18", status: "working", statusText: "処理中", owner: "鈴木", due: "7月15日" },
    { id: "AP-2026-07129", name: "山本 直子", kana: "ヤマモト ナオコ", kind: "国民健康保険", received: "7月13日 14:53", status: "alert", statusText: "要確認", owner: "未設定", due: "本日" },
    { id: "AP-2026-07128", name: "鈴木 大輔", kana: "スズキ ダイスケ", kind: "納税証明", received: "7月13日 13:07", status: "done", statusText: "完了", owner: "伊藤", due: "—" },
    { id: "AP-2026-07127", name: "伊藤 さくら", kana: "イトウ サクラ", kind: "転入届", received: "7月13日 11:32", status: "working", statusText: "処理中", owner: "高橋", due: "7月16日" },
    { id: "AP-2026-07126", name: "中村 剛", kana: "ナカムラ ツヨシ", kind: "児童手当", received: "7月13日 10:44", status: "waiting", statusText: "確認待ち", owner: "鈴木", due: "7月15日" },
    { id: "AP-2026-07125", name: "小林 恵", kana: "コバヤシ メグミ", kind: "介護保険", received: "7月13日 09:21", status: "alert", statusText: "書類不足", owner: "伊藤", due: "本日" },
    { id: "AP-2026-07124", name: "加藤 翔太", kana: "カトウ ショウタ", kind: "印鑑登録", received: "7月12日 18:06", status: "done", statusText: "完了", owner: "高橋", due: "—" },
  ];

  const statusIcon = (status) => {
    if (status === "done") return icon("complete", "status-icon");
    if (status === "alert") return icon("attention", "status-icon");
    if (status === "waiting") return icon("application", "status-icon");
    return icon("update", "status-icon");
  };

  const rowMarkup = rows.map((row) => `
    <tr data-status="${row.status}" data-search="${row.id} ${row.name} ${row.kana} ${row.kind}">
      <td class="check-cell"><input type="checkbox" aria-label="${row.id}を選択"></td>
      <td><a class="application-id" href="#">${row.id}</a></td>
      <td><strong>${row.name}</strong><span class="cell-sub">${row.kana}</span></td>
      <td><span class="kind-chip">${row.kind}</span></td>
      <td>${row.received}</td>
      <td><span class="status status-${row.status}">${statusIcon(row.status)}<span>${row.statusText}</span></span></td>
      <td><span class="owner ${row.owner === "未設定" ? "unassigned" : ""}">${row.owner}</span></td>
      <td class="due ${row.due === "本日" ? "due-today" : ""}">${row.due}</td>
      <td><button class="row-action" type="button" aria-label="${row.id}の操作メニュー">•••</button></td>
    </tr>
  `).join("");

  document.querySelector("#app").innerHTML = `
    <div class="app-shell">
      <aside class="sidebar" id="sidebar">
        <div class="brand">
          <span class="brand-mark">申</span>
          <span><strong>申請管理</strong><small>市民サービス基盤</small></span>
        </div>
        <nav aria-label="メインナビゲーション">
          <p class="nav-heading">業務メニュー</p>
          <a class="nav-item is-current" href="#">${icon("application")}<span>申請一覧</span><span class="nav-count">38</span></a>
          <a class="nav-item" href="#">${icon("documents")}<span>書類確認</span><span class="nav-count nav-count-alert">7</span></a>
          <a class="nav-item" href="#">${icon("family")}<span>子育て・世帯</span></a>
          <a class="nav-item" href="#">${icon("health")}<span>健康・福祉</span></a>
          <a class="nav-item" href="#">${icon("tax")}<span>税・納付</span></a>
          <p class="nav-heading nav-heading-secondary">システム</p>
          <a class="nav-item" href="#">${icon("update")}<span>処理履歴</span></a>
          <a class="nav-item" href="#">${icon("me")}<span>担当者設定</span></a>
        </nav>
        <div class="sidebar-footer">
          <span class="system-dot"></span>
          <span><strong>システム正常</strong><small>最終同期 17:02</small></span>
        </div>
      </aside>

      <div class="workspace">
        <header class="topbar">
          <button class="mobile-menu" type="button" aria-label="メニューを開く" aria-controls="sidebar" aria-expanded="false">☰</button>
          <div class="environment"><span>本番環境</span><strong>青葉市</strong></div>
          <div class="topbar-actions">
            <button class="notification-button ${isSkilled ? "skill-compliant" : ""}" type="button" ${isSkilled ? 'aria-label="通知、未読3件"' : 'title="通知"'}>
              ${icon("notification")}
              <span class="notification-badge">3</span>
            </button>
            <button class="user-menu" type="button" aria-label="ユーザーメニュー">
              <span class="avatar">深</span>
              <span class="user-copy"><strong>深水 拓郎</strong><small>申請管理者</small></span>
              <span aria-hidden="true">⌄</span>
            </button>
          </div>
        </header>

        <main class="main-content">
          <div class="breadcrumb"><a href="#">ホーム</a><span>/</span><span>オンライン申請</span></div>
          <div class="page-heading">
            <div>
              <h1>オンライン申請一覧</h1>
              <p>受け付けた申請の確認、担当割り当て、処理状況の更新を行います。</p>
            </div>
            <div class="heading-actions">
              <button class="button button-secondary" type="button">CSV出力</button>
              <button class="button button-primary" type="button">申請を新規登録</button>
            </div>
          </div>

          <section class="notice" aria-labelledby="notice-title">
            ${icon("attention", "notice-icon")}
            <div><strong id="notice-title">本日が処理期限の申請が3件あります</strong><p>未担当の申請を優先して確認してください。</p></div>
            <a href="#">対象を表示</a>
          </section>

          <section class="metrics" aria-label="申請状況の概要">
            <div class="metric"><span class="metric-icon">${icon("application")}</span><span><small>未処理</small><strong>38</strong></span><em>前日比 +5</em></div>
            <div class="metric"><span class="metric-icon">${icon("update")}</span><span><small>処理中</small><strong>12</strong></span><em>4人が対応中</em></div>
            <div class="metric"><span class="metric-icon">${icon("attention")}</span><span><small>要確認</small><strong>7</strong></span><em class="metric-alert">至急 3件</em></div>
            <div class="metric"><span class="metric-icon">${icon("complete")}</span><span><small>本日完了</small><strong>24</strong></span><em>平均 1.8日</em></div>
          </section>

          <section class="list-panel" aria-labelledby="list-title">
            <div class="filters">
              <label class="search-field"><span>申請を検索</span><span class="input-wrap">${icon("search")}<input id="search" type="search" placeholder="受付番号・氏名・申請種別"></span></label>
              <label><span>担当者</span><select><option>すべての担当者</option><option>高橋</option><option>鈴木</option><option>伊藤</option><option>未設定</option></select></label>
              <label><span>受付日</span><select><option>過去7日間</option><option>本日</option><option>過去30日間</option></select></label>
              <button class="button button-filter" type="button">条件をクリア</button>
            </div>

            <div class="tabs" role="tablist" aria-label="処理状況">
              <button role="tab" aria-selected="true" data-filter="all">すべて <span>93</span></button>
              <button role="tab" aria-selected="false" data-filter="waiting">確認待ち <span>38</span></button>
              <button role="tab" aria-selected="false" data-filter="working">処理中 <span>12</span></button>
              <button role="tab" aria-selected="false" data-filter="alert">要確認 <span>7</span></button>
              <button role="tab" aria-selected="false" data-filter="done">完了 <span>36</span></button>
            </div>

            <div class="table-heading"><div><h2 id="list-title">申請一覧</h2><span id="result-count">93件中 1–8件</span></div><button class="density-control" type="button">表示密度：標準</button></div>
            <div class="table-scroll">
              <table>
                <thead><tr><th class="check-cell"><input id="select-all" type="checkbox" aria-label="表示中の申請をすべて選択"></th><th>受付番号</th><th>申請者</th><th>申請種別</th><th>受付日時</th><th>処理状況</th><th>担当</th><th>期限</th><th><span class="visually-hidden">操作</span></th></tr></thead>
                <tbody>${rowMarkup}</tbody>
              </table>
            </div>
            <div class="table-footer">
              <span>1ページあたり <select aria-label="1ページあたりの表示件数"><option>20件</option><option>50件</option></select></span>
              <nav class="pagination" aria-label="ページネーション"><button type="button" disabled>‹</button><button class="is-page" type="button" aria-current="page">1</button><button type="button">2</button><button type="button">3</button><span>…</span><button type="button">12</button><button type="button">›</button></nav>
            </div>
          </section>
        </main>
      </div>
    </div>
    <div class="selection-bar" aria-live="polite"><strong><span id="selected-count">0</span>件を選択中</strong><button type="button">担当者を割り当て</button><button type="button">ステータスを更新</button></div>
  `;

  const sidebar = document.querySelector("#sidebar");
  const menuButton = document.querySelector(".mobile-menu");
  menuButton.addEventListener("click", () => {
    const open = sidebar.classList.toggle("is-open");
    menuButton.setAttribute("aria-expanded", String(open));
  });

  const tableRows = [...document.querySelectorAll("tbody tr")];
  const searchInput = document.querySelector("#search");
  let activeFilter = "all";

  const applyFilters = () => {
    const query = searchInput.value.trim().toLocaleLowerCase("ja");
    let visible = 0;
    tableRows.forEach((row) => {
      const filterMatch = activeFilter === "all" || row.dataset.status === activeFilter;
      const searchMatch = !query || row.dataset.search.toLocaleLowerCase("ja").includes(query);
      row.hidden = !(filterMatch && searchMatch);
      if (!row.hidden) visible += 1;
    });
    document.querySelector("#result-count").textContent = `${visible}件を表示`;
  };

  searchInput.addEventListener("input", applyFilters);
  document.querySelectorAll("[role='tab']").forEach((tab) => {
    tab.addEventListener("click", () => {
      document.querySelectorAll("[role='tab']").forEach((item) => item.setAttribute("aria-selected", "false"));
      tab.setAttribute("aria-selected", "true");
      activeFilter = tab.dataset.filter;
      applyFilters();
    });
  });

  const checkboxes = [...document.querySelectorAll("tbody input[type='checkbox']")];
  const selectionBar = document.querySelector(".selection-bar");
  const updateSelection = () => {
    const count = checkboxes.filter((checkbox) => checkbox.checked).length;
    document.querySelector("#selected-count").textContent = count;
    selectionBar.classList.toggle("is-visible", count > 0);
  };
  checkboxes.forEach((checkbox) => checkbox.addEventListener("change", updateSelection));
  document.querySelector("#select-all").addEventListener("change", (event) => {
    checkboxes.forEach((checkbox) => {
      const row = checkbox.closest("tr");
      if (!row.hidden) checkbox.checked = event.target.checked;
    });
    updateSelection();
  });
})();
